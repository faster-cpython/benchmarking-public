# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_11_9
- machine: linux-x86_64
- commit hash: 50321ce
- commit date: 2025-06-30
- overall geometric mean: 1.067x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.02x faster                                               |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                             |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                              |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                               |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 637 ms: 1.35x faster                                               |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                               |
| async_generators           | 433 ms                                                 | 431 ms: 1.00x faster                                               |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                              |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.2 ms: 1.19x faster                                              |
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                               |
| nbody          | 87.7 ms                                                | 95.8 ms: 1.09x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.14 ms: 1.20x faster                                              |
| regex_v8       | 26.9 ms                                                | 22.6 ms: 1.19x faster                                              |
| regex_dna      | 220 ms                                                 | 198 ms: 1.11x faster                                               |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.13x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.82 sec: 1.16x faster                                             |
| unpickle_pure_python | 213 us                                                 | 192 us: 1.11x faster                                               |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 55.4 ms: 1.09x faster                                              |
| xml_etree_generate   | 86.8 ms                                                | 79.8 ms: 1.09x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 98.4 ms: 1.03x faster                                              |
| json_loads           | 27.2 us                                                | 28.4 us: 1.04x slower                                              |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.10x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                              |
| python_startup_no_site | 7.00 ms                                                | 6.94 ms: 1.01x faster                                              |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                              |
| mako            | 10.7 ms                                                | 10.5 ms: 1.02x faster                                              |
| genshi_xml      | 50.5 ms                                                | 49.7 ms: 1.02x faster                                              |
| django_template | 31.7 ms                                                | 32.4 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                               |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                               |
| richards                   | 47.5 ms                                                | 34.7 ms: 1.37x faster                                              |
| deepcopy                   | 354 us                                                 | 260 us: 1.37x faster                                               |
| richards_super             | 53.7 ms                                                | 39.7 ms: 1.35x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 637 ms: 1.35x faster                                               |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 29.6 us: 1.30x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                               |
| spectral_norm              | 113 ms                                                 | 92.6 ms: 1.22x faster                                              |
| go                         | 141 ms                                                 | 116 ms: 1.22x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.14 ms: 1.20x faster                                              |
| scimark_fft                | 367 ms                                                 | 308 ms: 1.19x faster                                               |
| regex_v8                   | 26.9 ms                                                | 22.6 ms: 1.19x faster                                              |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                              |
| float                      | 78.7 ms                                                | 66.2 ms: 1.19x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.16x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.82 sec: 1.16x faster                                             |
| pyflate                    | 470 ms                                                 | 417 ms: 1.13x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                               |
| unpickle_pure_python       | 213 us                                                 | 192 us: 1.11x faster                                               |
| regex_dna                  | 220 ms                                                 | 198 ms: 1.11x faster                                               |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 55.4 ms: 1.09x faster                                              |
| telco                      | 8.40 ms                                                | 7.72 ms: 1.09x faster                                              |
| xml_etree_generate         | 86.8 ms                                                | 79.8 ms: 1.09x faster                                              |
| dulwich_log                | 64.6 ms                                                | 59.5 ms: 1.09x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.37 sec: 1.07x faster                                             |
| crypto_pyaes               | 74.7 ms                                                | 70.8 ms: 1.06x faster                                              |
| deltablue                  | 3.19 ms                                                | 3.03 ms: 1.05x faster                                              |
| thrift                     | 800 us                                                 | 761 us: 1.05x faster                                               |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                              |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.05x faster                                             |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                             |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                              |
| pprint_pformat             | 1.48 sec                                               | 1.43 sec: 1.04x faster                                             |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 98.4 ms: 1.03x faster                                              |
| 2to3                       | 266 ms                                                 | 259 ms: 1.02x faster                                               |
| scimark_monte_carlo        | 66.8 ms                                                | 65.3 ms: 1.02x faster                                              |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.92 ms: 1.02x faster                                              |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                               |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                             |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                               |
| mako                       | 10.7 ms                                                | 10.5 ms: 1.02x faster                                              |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                              |
| sympy_integrate            | 19.8 ms                                                | 19.5 ms: 1.02x faster                                              |
| pprint_safe_repr           | 727 ms                                                 | 715 ms: 1.02x faster                                               |
| genshi_xml                 | 50.5 ms                                                | 49.7 ms: 1.02x faster                                              |
| json                       | 5.32 ms                                                | 5.26 ms: 1.01x faster                                              |
| pathlib                    | 17.4 ms                                                | 17.2 ms: 1.01x faster                                              |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                              |
| logging_simple             | 5.65 us                                                | 5.60 us: 1.01x faster                                              |
| python_startup_no_site     | 7.00 ms                                                | 6.94 ms: 1.01x faster                                              |
| async_generators           | 433 ms                                                 | 431 ms: 1.00x faster                                               |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                               |
| fannkuch                   | 394 ms                                                 | 397 ms: 1.01x slower                                               |
| shortest_path              | 487 ms                                                 | 491 ms: 1.01x slower                                               |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                               |
| gc_traversal               | 4.90 ms                                                | 4.97 ms: 1.02x slower                                              |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                               |
| logging_silent             | 101 ns                                                 | 103 ns: 1.02x slower                                               |
| sympy_expand               | 456 ms                                                 | 465 ms: 1.02x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.21 ms: 1.02x slower                                              |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                             |
| django_template            | 31.7 ms                                                | 32.4 ms: 1.02x slower                                              |
| connected_components       | 447 ms                                                 | 458 ms: 1.03x slower                                               |
| nqueens                    | 80.9 ms                                                | 83.2 ms: 1.03x slower                                              |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                               |
| generators                 | 28.8 ms                                                | 30.0 ms: 1.04x slower                                              |
| json_loads                 | 27.2 us                                                | 28.4 us: 1.04x slower                                              |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                               |
| coverage                   | 82.8 ms                                                | 87.2 ms: 1.05x slower                                              |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.05x slower                                              |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                               |
| chaos                      | 58.0 ms                                                | 61.8 ms: 1.07x slower                                              |
| nbody                      | 87.7 ms                                                | 95.8 ms: 1.09x slower                                              |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.10x slower                                              |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                              |
| many_optionals             | 857 us                                                 | 986 us: 1.15x slower                                               |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.53x slower                                              |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                       |

Benchmark hidden because not significant (4): logging_format, sympy_str, asyncio_websockets, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250630-3.15.0a0-50321ce-JIT/bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.067x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x