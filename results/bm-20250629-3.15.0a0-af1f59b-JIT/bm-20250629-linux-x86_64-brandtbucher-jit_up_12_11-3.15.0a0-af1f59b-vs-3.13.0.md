# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_12_11
- machine: linux-x86_64
- commit hash: af1f59b
- commit date: 2025-06-29
- overall geometric mean: 1.066x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                                |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                              |
| html5lib       | 63.4 ms                                                | 61.5 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.40x faster                                                |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.34x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 496 ms: 1.10x faster                                                |
| async_generators           | 433 ms                                                 | 430 ms: 1.01x faster                                                |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.01x slower                                                |
| coroutines                 | 22.2 ms                                                | 24.7 ms: 1.11x slower                                               |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.7 ms: 1.20x faster                                               |
| pidigits       | 186 ms                                                 | 193 ms: 1.03x slower                                                |
| nbody          | 87.7 ms                                                | 100 ms: 1.14x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 24.0 ms: 1.12x faster                                               |
| regex_effbot   | 3.77 ms                                                | 3.41 ms: 1.10x faster                                               |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.81 sec: 1.17x faster                                              |
| unpickle_pure_python | 213 us                                                 | 189 us: 1.13x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                |
| xml_etree_process    | 60.5 ms                                                | 55.4 ms: 1.09x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 79.7 ms: 1.09x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 99.0 ms: 1.02x faster                                               |
| json_loads           | 27.2 us                                                | 28.1 us: 1.03x slower                                               |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.09x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                               |
| python_startup_no_site | 7.00 ms                                                | 6.95 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                               |
| genshi_xml      | 50.5 ms                                                | 49.7 ms: 1.02x faster                                               |
| mako            | 10.7 ms                                                | 10.6 ms: 1.01x faster                                               |
| django_template | 31.7 ms                                                | 32.9 ms: 1.04x slower                                               |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                              |
| richards                   | 47.5 ms                                                | 30.3 ms: 1.57x faster                                               |
| richards_super             | 53.7 ms                                                | 35.7 ms: 1.51x faster                                               |
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.40x faster                                                |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                |
| deepcopy                   | 354 us                                                 | 258 us: 1.37x faster                                                |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.34x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 29.5 us: 1.30x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                |
| spectral_norm              | 113 ms                                                 | 88.7 ms: 1.28x faster                                               |
| go                         | 141 ms                                                 | 115 ms: 1.22x faster                                                |
| float                      | 78.7 ms                                                | 65.7 ms: 1.20x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                               |
| scimark_fft                | 367 ms                                                 | 311 ms: 1.18x faster                                                |
| tomli_loads                | 2.12 sec                                               | 1.81 sec: 1.17x faster                                              |
| pyflate                    | 470 ms                                                 | 403 ms: 1.17x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                |
| unpickle_pure_python       | 213 us                                                 | 189 us: 1.13x faster                                                |
| regex_v8                   | 26.9 ms                                                | 24.0 ms: 1.12x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.41 ms: 1.10x faster                                               |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 496 ms: 1.10x faster                                                |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                |
| xml_etree_process          | 60.5 ms                                                | 55.4 ms: 1.09x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 79.7 ms: 1.09x faster                                               |
| dulwich_log                | 64.6 ms                                                | 59.3 ms: 1.09x faster                                               |
| telco                      | 8.40 ms                                                | 7.74 ms: 1.09x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.34 sec: 1.08x faster                                              |
| deltablue                  | 3.19 ms                                                | 3.03 ms: 1.05x faster                                               |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                              |
| thrift                     | 800 us                                                 | 768 us: 1.04x faster                                                |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                               |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.87 ms: 1.03x faster                                               |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                |
| html5lib                   | 63.4 ms                                                | 61.5 ms: 1.03x faster                                               |
| gc_traversal               | 4.90 ms                                                | 4.76 ms: 1.03x faster                                               |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.03x faster                                               |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 99.0 ms: 1.02x faster                                               |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                                |
| json                       | 5.32 ms                                                | 5.21 ms: 1.02x faster                                               |
| comprehensions             | 16.5 us                                                | 16.2 us: 1.02x faster                                               |
| genshi_xml                 | 50.5 ms                                                | 49.7 ms: 1.02x faster                                               |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.02x faster                                              |
| logging_simple             | 5.65 us                                                | 5.57 us: 1.02x faster                                               |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.01x faster                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 66.0 ms: 1.01x faster                                               |
| mako                       | 10.7 ms                                                | 10.6 ms: 1.01x faster                                               |
| python_startup_no_site     | 7.00 ms                                                | 6.95 ms: 1.01x faster                                               |
| async_generators           | 433 ms                                                 | 430 ms: 1.01x faster                                                |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.01x slower                                                |
| logging_format             | 6.23 us                                                | 6.27 us: 1.01x slower                                               |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                                |
| pathlib                    | 17.4 ms                                                | 17.5 ms: 1.01x slower                                               |
| crypto_pyaes               | 74.7 ms                                                | 75.7 ms: 1.01x slower                                               |
| nqueens                    | 80.9 ms                                                | 82.1 ms: 1.01x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.17 ms: 1.02x slower                                               |
| sympy_expand               | 456 ms                                                 | 465 ms: 1.02x slower                                                |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                              |
| logging_silent             | 101 ns                                                 | 103 ns: 1.02x slower                                                |
| connected_components       | 447 ms                                                 | 458 ms: 1.03x slower                                                |
| json_loads                 | 27.2 us                                                | 28.1 us: 1.03x slower                                               |
| pidigits                   | 186 ms                                                 | 193 ms: 1.03x slower                                                |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                |
| django_template            | 31.7 ms                                                | 32.9 ms: 1.04x slower                                               |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.57 ms: 1.05x slower                                               |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                |
| chaos                      | 58.0 ms                                                | 61.6 ms: 1.06x slower                                               |
| generators                 | 28.8 ms                                                | 30.6 ms: 1.06x slower                                               |
| coverage                   | 82.8 ms                                                | 88.1 ms: 1.06x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.09x slower                                               |
| coroutines                 | 22.2 ms                                                | 24.7 ms: 1.11x slower                                               |
| many_optionals             | 857 us                                                 | 977 us: 1.14x slower                                                |
| nbody                      | 87.7 ms                                                | 100 ms: 1.14x slower                                                |
| subparsers                 | 15.5 ms                                                | 23.8 ms: 1.54x slower                                               |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                        |

Benchmark hidden because not significant (5): sphinx, pprint_safe_repr, sympy_str, fannkuch, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250629-3.15.0a0-af1f59b-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.066x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x