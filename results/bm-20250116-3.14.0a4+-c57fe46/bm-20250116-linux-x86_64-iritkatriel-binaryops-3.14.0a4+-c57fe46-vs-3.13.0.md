# Results vs. 3.13.0

- fork: iritkatriel
- ref: binaryops
- machine: linux-x86_64
- commit hash: c57fe46
- commit date: 2025-01-16
- overall geometric mean: 1.042x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                             |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.00x slower                                           |
| html5lib       | 63.4 ms                                                | 61.7 ms: 1.03x faster                                            |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                             |
| async_tree_io_tg           | 861 ms                                                 | 590 ms: 1.46x faster                                             |
| async_tree_io              | 838 ms                                                 | 606 ms: 1.38x faster                                             |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                             |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 470 ms: 1.16x faster                                             |
| async_generators           | 433 ms                                                 | 384 ms: 1.13x faster                                             |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                            |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.0 ms: 1.09x faster                                            |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                             |
| nbody          | 87.7 ms                                                | 95.2 ms: 1.09x slower                                            |
| Geometric mean | (ref)                                                  | 1.00x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.29 ms: 1.15x faster                                            |
| regex_v8       | 26.9 ms                                                | 25.7 ms: 1.04x faster                                            |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                             |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                             |
| tomli_loads          | 2.12 sec                                               | 1.97 sec: 1.07x faster                                           |
| xml_etree_iterparse  | 101 ms                                                 | 97.3 ms: 1.04x faster                                            |
| xml_etree_generate   | 86.8 ms                                                | 85.3 ms: 1.02x faster                                            |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                             |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                             |
| json_loads           | 27.2 us                                                | 29.4 us: 1.08x slower                                            |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.17x slower                                            |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                     |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.08 ms: 1.01x slower                                            |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                            |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 48.2 ms: 1.05x faster                                            |
| genshi_text     | 22.6 ms                                                | 21.7 ms: 1.04x faster                                            |
| django_template | 31.7 ms                                                | 32.1 ms: 1.01x slower                                            |
| mako            | 10.7 ms                                                | 11.8 ms: 1.10x slower                                            |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                             |
| async_tree_io_tg           | 861 ms                                                 | 590 ms: 1.46x faster                                             |
| async_tree_io              | 838 ms                                                 | 606 ms: 1.38x faster                                             |
| deepcopy                   | 354 us                                                 | 258 us: 1.37x faster                                             |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                             |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                             |
| deepcopy_memo              | 38.4 us                                                | 31.3 us: 1.23x faster                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.65 us: 1.22x faster                                            |
| go                         | 141 ms                                                 | 118 ms: 1.19x faster                                             |
| spectral_norm              | 113 ms                                                 | 96.0 ms: 1.18x faster                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 470 ms: 1.16x faster                                             |
| regex_effbot               | 3.77 ms                                                | 3.29 ms: 1.15x faster                                            |
| pylint                     | 312 ms                                                 | 277 ms: 1.13x faster                                             |
| async_generators           | 433 ms                                                 | 384 ms: 1.13x faster                                             |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                             |
| float                      | 78.7 ms                                                | 72.0 ms: 1.09x faster                                            |
| telco                      | 8.40 ms                                                | 7.76 ms: 1.08x faster                                            |
| tomli_loads                | 2.12 sec                                               | 1.97 sec: 1.07x faster                                           |
| scimark_fft                | 367 ms                                                 | 343 ms: 1.07x faster                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.71 ms: 1.07x faster                                            |
| richards                   | 47.5 ms                                                | 44.6 ms: 1.07x faster                                            |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                            |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                           |
| thrift                     | 800 us                                                 | 759 us: 1.05x faster                                             |
| richards_super             | 53.7 ms                                                | 51.2 ms: 1.05x faster                                            |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                             |
| generators                 | 28.8 ms                                                | 27.5 ms: 1.05x faster                                            |
| genshi_xml                 | 50.5 ms                                                | 48.2 ms: 1.05x faster                                            |
| regex_v8                   | 26.9 ms                                                | 25.7 ms: 1.04x faster                                            |
| genshi_text                | 22.6 ms                                                | 21.7 ms: 1.04x faster                                            |
| xml_etree_iterparse        | 101 ms                                                 | 97.3 ms: 1.04x faster                                            |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.51 sec: 1.04x faster                                           |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                            |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                             |
| logging_simple             | 5.65 us                                                | 5.45 us: 1.04x faster                                            |
| logging_format             | 6.23 us                                                | 6.03 us: 1.03x faster                                            |
| html5lib                   | 63.4 ms                                                | 61.7 ms: 1.03x faster                                            |
| sqlglot_normalize          | 108 ms                                                 | 105 ms: 1.03x faster                                             |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.5 ms: 1.02x faster                                            |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                             |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                             |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                             |
| mdp                        | 2.54 sec                                               | 2.49 sec: 1.02x faster                                           |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                           |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                             |
| xml_etree_generate         | 86.8 ms                                                | 85.3 ms: 1.02x faster                                            |
| connected_components       | 447 ms                                                 | 440 ms: 1.02x faster                                             |
| shortest_path              | 487 ms                                                 | 481 ms: 1.01x faster                                             |
| sqlglot_optimize           | 53.4 ms                                                | 52.8 ms: 1.01x faster                                            |
| regex_dna                  | 220 ms                                                 | 218 ms: 1.01x faster                                             |
| crypto_pyaes               | 74.7 ms                                                | 74.0 ms: 1.01x faster                                            |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                             |
| dulwich_log                | 64.6 ms                                                | 64.2 ms: 1.01x faster                                            |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                             |
| sqlglot_parse              | 1.26 ms                                                | 1.27 ms: 1.00x slower                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 67.1 ms: 1.00x slower                                            |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.00x slower                                           |
| pprint_safe_repr           | 727 ms                                                 | 731 ms: 1.01x slower                                             |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                            |
| gc_traversal               | 4.90 ms                                                | 4.93 ms: 1.01x slower                                            |
| pyflate                    | 470 ms                                                 | 474 ms: 1.01x slower                                             |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                             |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                            |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                             |
| python_startup_no_site     | 7.00 ms                                                | 7.08 ms: 1.01x slower                                            |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.01x slower                                           |
| django_template            | 31.7 ms                                                | 32.1 ms: 1.01x slower                                            |
| deltablue                  | 3.19 ms                                                | 3.25 ms: 1.02x slower                                            |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                            |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                             |
| fannkuch                   | 394 ms                                                 | 403 ms: 1.02x slower                                             |
| hexiom                     | 6.08 ms                                                | 6.24 ms: 1.03x slower                                            |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                            |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                             |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                            |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                             |
| bench_thread_pool          | 818 us                                                 | 867 us: 1.06x slower                                             |
| json_loads                 | 27.2 us                                                | 29.4 us: 1.08x slower                                            |
| nbody                      | 87.7 ms                                                | 95.2 ms: 1.09x slower                                            |
| coverage                   | 82.8 ms                                                | 90.4 ms: 1.09x slower                                            |
| logging_silent             | 101 ns                                                 | 111 ns: 1.10x slower                                             |
| mako                       | 10.7 ms                                                | 11.8 ms: 1.10x slower                                            |
| many_optionals             | 857 us                                                 | 946 us: 1.10x slower                                             |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.17x slower                                            |
| subparsers                 | 15.5 ms                                                | 20.4 ms: 1.32x slower                                            |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                     |

Benchmark hidden because not significant (7): json, nqueens, sympy_expand, asyncio_websockets, chaos, sympy_integrate, xml_etree_process
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x