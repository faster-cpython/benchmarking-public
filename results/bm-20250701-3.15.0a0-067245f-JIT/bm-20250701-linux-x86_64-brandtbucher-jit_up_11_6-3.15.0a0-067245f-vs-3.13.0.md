# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_11_6
- machine: linux-x86_64
- commit hash: 067245f
- commit date: 2025-07-01
- overall geometric mean: 1.064x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                               |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.02x slower                                             |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                               |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 639 ms: 1.35x faster                                               |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                               |
| async_generators           | 433 ms                                                 | 424 ms: 1.02x faster                                               |
| coroutines                 | 22.2 ms                                                | 25.4 ms: 1.14x slower                                              |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.6 ms: 1.20x faster                                              |
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                               |
| nbody          | 87.7 ms                                                | 93.6 ms: 1.07x slower                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.8 ms: 1.13x faster                                              |
| regex_effbot   | 3.77 ms                                                | 3.43 ms: 1.10x faster                                              |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                               |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.82 sec: 1.17x faster                                             |
| unpickle_pure_python | 213 us                                                 | 190 us: 1.12x faster                                               |
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 55.8 ms: 1.08x faster                                              |
| xml_etree_generate   | 86.8 ms                                                | 80.2 ms: 1.08x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 99.3 ms: 1.02x faster                                              |
| json_loads           | 27.2 us                                                | 28.0 us: 1.03x slower                                              |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.07x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.08x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                              |
| python_startup_no_site | 7.00 ms                                                | 6.95 ms: 1.01x faster                                              |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                              |
| mako            | 10.7 ms                                                | 10.4 ms: 1.02x faster                                              |
| genshi_xml      | 50.5 ms                                                | 50.1 ms: 1.01x faster                                              |
| django_template | 31.7 ms                                                | 32.4 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                               |
| richards                   | 47.5 ms                                                | 33.7 ms: 1.41x faster                                              |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                               |
| richards_super             | 53.7 ms                                                | 38.9 ms: 1.38x faster                                              |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 639 ms: 1.35x faster                                               |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.31x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                               |
| spectral_norm              | 113 ms                                                 | 90.0 ms: 1.26x faster                                              |
| go                         | 141 ms                                                 | 114 ms: 1.24x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.21x faster                                              |
| float                      | 78.7 ms                                                | 65.6 ms: 1.20x faster                                              |
| scimark_fft                | 367 ms                                                 | 313 ms: 1.17x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.82 sec: 1.17x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                               |
| pyflate                    | 470 ms                                                 | 415 ms: 1.13x faster                                               |
| regex_v8                   | 26.9 ms                                                | 23.8 ms: 1.13x faster                                              |
| unpickle_pure_python       | 213 us                                                 | 190 us: 1.12x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.43 ms: 1.10x faster                                              |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 55.8 ms: 1.08x faster                                              |
| telco                      | 8.40 ms                                                | 7.75 ms: 1.08x faster                                              |
| xml_etree_generate         | 86.8 ms                                                | 80.2 ms: 1.08x faster                                              |
| dulwich_log                | 64.6 ms                                                | 60.0 ms: 1.08x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.37 sec: 1.07x faster                                             |
| pprint_safe_repr           | 727 ms                                                 | 691 ms: 1.05x faster                                               |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                              |
| k_core                     | 2.37 sec                                               | 2.25 sec: 1.05x faster                                             |
| deltablue                  | 3.19 ms                                                | 3.04 ms: 1.05x faster                                              |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                             |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                               |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                               |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                              |
| pprint_pformat             | 1.48 sec                                               | 1.43 sec: 1.04x faster                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.87 ms: 1.03x faster                                              |
| json                       | 5.32 ms                                                | 5.17 ms: 1.03x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.82 us: 1.03x faster                                              |
| scimark_monte_carlo        | 66.8 ms                                                | 65.0 ms: 1.03x faster                                              |
| thrift                     | 800 us                                                 | 779 us: 1.03x faster                                               |
| crypto_pyaes               | 74.7 ms                                                | 72.8 ms: 1.03x faster                                              |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                              |
| mako                       | 10.7 ms                                                | 10.4 ms: 1.02x faster                                              |
| logging_simple             | 5.65 us                                                | 5.53 us: 1.02x faster                                              |
| async_generators           | 433 ms                                                 | 424 ms: 1.02x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 99.3 ms: 1.02x faster                                              |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                               |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                               |
| sympy_integrate            | 19.8 ms                                                | 19.5 ms: 1.02x faster                                              |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                               |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                              |
| python_startup_no_site     | 7.00 ms                                                | 6.95 ms: 1.01x faster                                              |
| genshi_xml                 | 50.5 ms                                                | 50.1 ms: 1.01x faster                                              |
| pathlib                    | 17.4 ms                                                | 17.2 ms: 1.01x faster                                              |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                               |
| shortest_path              | 487 ms                                                 | 494 ms: 1.02x slower                                               |
| fannkuch                   | 394 ms                                                 | 401 ms: 1.02x slower                                               |
| nqueens                    | 80.9 ms                                                | 82.4 ms: 1.02x slower                                              |
| sympy_expand               | 456 ms                                                 | 467 ms: 1.02x slower                                               |
| django_template            | 31.7 ms                                                | 32.4 ms: 1.02x slower                                              |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.02x slower                                             |
| hexiom                     | 6.08 ms                                                | 6.25 ms: 1.03x slower                                              |
| json_loads                 | 27.2 us                                                | 28.0 us: 1.03x slower                                              |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                               |
| connected_components       | 447 ms                                                 | 462 ms: 1.03x slower                                               |
| logging_silent             | 101 ns                                                 | 105 ns: 1.04x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                               |
| scimark_lu                 | 114 ms                                                 | 120 ms: 1.05x slower                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.57 ms: 1.05x slower                                              |
| generators                 | 28.8 ms                                                | 30.2 ms: 1.05x slower                                              |
| coverage                   | 82.8 ms                                                | 87.4 ms: 1.05x slower                                              |
| chaos                      | 58.0 ms                                                | 61.5 ms: 1.06x slower                                              |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.07x slower                                               |
| nbody                      | 87.7 ms                                                | 93.6 ms: 1.07x slower                                              |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.08x slower                                              |
| coroutines                 | 22.2 ms                                                | 25.4 ms: 1.14x slower                                              |
| many_optionals             | 857 us                                                 | 991 us: 1.16x slower                                               |
| subparsers                 | 15.5 ms                                                | 24.0 ms: 1.55x slower                                              |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                       |

Benchmark hidden because not significant (7): sphinx, gc_traversal, logging_format, sympy_str, sympy_sum, asyncio_websockets, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250701-3.15.0a0-067245f-JIT/bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x