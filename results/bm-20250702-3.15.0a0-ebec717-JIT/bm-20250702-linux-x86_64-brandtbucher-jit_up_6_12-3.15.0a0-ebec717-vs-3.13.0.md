# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_6_12
- machine: linux-x86_64
- commit hash: ebec717
- commit date: 2025-07-02
- overall geometric mean: 1.025x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 263 ms: 1.01x faster                                               |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                             |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                              |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.00x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 323 ms: 1.43x faster                                               |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                               |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 641 ms: 1.34x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 504 ms: 1.08x faster                                               |
| async_generators           | 433 ms                                                 | 431 ms: 1.01x faster                                               |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                              |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.3 ms: 1.20x faster                                              |
| nbody          | 87.7 ms                                                | 94.1 ms: 1.07x slower                                              |
| pidigits       | 186 ms                                                 | 201 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.5 ms: 1.19x faster                                              |
| regex_effbot   | 3.77 ms                                                | 3.20 ms: 1.18x faster                                              |
| regex_dna      | 220 ms                                                 | 206 ms: 1.07x faster                                               |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.11x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                             |
| unpickle_pure_python | 213 us                                                 | 190 us: 1.12x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 55.1 ms: 1.10x faster                                              |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 79.7 ms: 1.09x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 98.9 ms: 1.02x faster                                              |
| json_loads           | 27.2 us                                                | 28.1 us: 1.03x slower                                              |
| pickle_pure_python   | 302 us                                                 | 327 us: 1.08x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.10x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                              |
| python_startup_no_site | 7.00 ms                                                | 6.96 ms: 1.01x faster                                              |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.2 ms: 1.06x faster                                              |
| mako            | 10.7 ms                                                | 10.6 ms: 1.01x faster                                              |
| django_template | 31.7 ms                                                | 32.8 ms: 1.04x slower                                              |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                             |
| richards                   | 47.5 ms                                                | 32.0 ms: 1.49x faster                                              |
| richards_super             | 53.7 ms                                                | 36.2 ms: 1.49x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 323 ms: 1.43x faster                                               |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                               |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                               |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 641 ms: 1.34x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 29.6 us: 1.30x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                               |
| go                         | 141 ms                                                 | 115 ms: 1.22x faster                                               |
| spectral_norm              | 113 ms                                                 | 93.1 ms: 1.22x faster                                              |
| float                      | 78.7 ms                                                | 65.3 ms: 1.20x faster                                              |
| regex_v8                   | 26.9 ms                                                | 22.5 ms: 1.19x faster                                              |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                              |
| regex_effbot               | 3.77 ms                                                | 3.20 ms: 1.18x faster                                              |
| scimark_fft                | 367 ms                                                 | 316 ms: 1.16x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                               |
| unpickle_pure_python       | 213 us                                                 | 190 us: 1.12x faster                                               |
| pyflate                    | 470 ms                                                 | 421 ms: 1.12x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 55.1 ms: 1.10x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 79.7 ms: 1.09x faster                                              |
| dulwich_log                | 64.6 ms                                                | 59.4 ms: 1.09x faster                                              |
| pylint                     | 312 ms                                                 | 287 ms: 1.09x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 504 ms: 1.08x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.36 sec: 1.07x faster                                             |
| regex_dna                  | 220 ms                                                 | 206 ms: 1.07x faster                                               |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.06x faster                                              |
| pprint_safe_repr           | 727 ms                                                 | 689 ms: 1.05x faster                                               |
| pprint_pformat             | 1.48 sec                                               | 1.41 sec: 1.05x faster                                             |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                             |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                               |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                              |
| thrift                     | 800 us                                                 | 775 us: 1.03x faster                                               |
| crypto_pyaes               | 74.7 ms                                                | 72.4 ms: 1.03x faster                                              |
| deltablue                  | 3.19 ms                                                | 3.10 ms: 1.03x faster                                              |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                               |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 98.9 ms: 1.02x faster                                              |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                              |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.02x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.86 us: 1.02x faster                                              |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.01x faster                                             |
| scimark_monte_carlo        | 66.8 ms                                                | 65.8 ms: 1.01x faster                                              |
| json                       | 5.32 ms                                                | 5.26 ms: 1.01x faster                                              |
| 2to3                       | 266 ms                                                 | 263 ms: 1.01x faster                                               |
| sympy_integrate            | 19.8 ms                                                | 19.7 ms: 1.01x faster                                              |
| comprehensions             | 16.5 us                                                | 16.4 us: 1.01x faster                                              |
| python_startup_no_site     | 7.00 ms                                                | 6.96 ms: 1.01x faster                                              |
| async_generators           | 433 ms                                                 | 431 ms: 1.01x faster                                               |
| mako                       | 10.7 ms                                                | 10.6 ms: 1.01x faster                                              |
| hexiom                     | 6.08 ms                                                | 6.13 ms: 1.01x slower                                              |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                               |
| logging_silent             | 101 ns                                                 | 102 ns: 1.01x slower                                               |
| logging_format             | 6.23 us                                                | 6.33 us: 1.02x slower                                              |
| sympy_sum                  | 150 ms                                                 | 154 ms: 1.02x slower                                               |
| fannkuch                   | 394 ms                                                 | 403 ms: 1.02x slower                                               |
| sympy_expand               | 456 ms                                                 | 467 ms: 1.02x slower                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.17 ms: 1.03x slower                                              |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                             |
| nqueens                    | 80.9 ms                                                | 83.5 ms: 1.03x slower                                              |
| json_loads                 | 27.2 us                                                | 28.1 us: 1.03x slower                                              |
| django_template            | 31.7 ms                                                | 32.8 ms: 1.04x slower                                              |
| connected_components       | 447 ms                                                 | 463 ms: 1.04x slower                                               |
| djangocms                  | 22.3 us                                                | 23.2 us: 1.04x slower                                              |
| scimark_lu                 | 114 ms                                                 | 120 ms: 1.05x slower                                               |
| gc_traversal               | 4.90 ms                                                | 5.13 ms: 1.05x slower                                              |
| chaos                      | 58.0 ms                                                | 61.0 ms: 1.05x slower                                              |
| generators                 | 28.8 ms                                                | 30.3 ms: 1.05x slower                                              |
| raytrace                   | 262 ms                                                 | 276 ms: 1.06x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                               |
| coverage                   | 82.8 ms                                                | 88.2 ms: 1.07x slower                                              |
| nbody                      | 87.7 ms                                                | 94.1 ms: 1.07x slower                                              |
| create_gc_cycles           | 2.45 ms                                                | 2.63 ms: 1.08x slower                                              |
| pidigits                   | 186 ms                                                 | 201 ms: 1.08x slower                                               |
| pickle_pure_python         | 302 us                                                 | 327 us: 1.08x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.10x slower                                              |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                              |
| many_optionals             | 857 us                                                 | 990 us: 1.16x slower                                               |
| subparsers                 | 15.5 ms                                                | 23.7 ms: 1.53x slower                                              |
| telco                      | 8.40 ms                                                | 160 ms: 19.11x slower                                              |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (4): genshi_xml, asyncio_websockets, sympy_str, logging_simple
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250702-3.15.0a0-ebec717-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x