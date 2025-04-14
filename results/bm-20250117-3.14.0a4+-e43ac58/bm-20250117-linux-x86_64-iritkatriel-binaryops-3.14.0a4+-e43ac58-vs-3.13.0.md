# Results vs. 3.13.0

- fork: iritkatriel
- ref: binaryops
- machine: linux-x86_64
- commit hash: e43ac58
- commit date: 2025-01-17
- overall geometric mean: 1.049x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                             |
| docutils       | 2.58 sec                                               | 2.59 sec: 1.00x slower                                           |
| html5lib       | 63.4 ms                                                | 60.9 ms: 1.04x faster                                            |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 304 ms: 1.52x faster                                             |
| async_tree_io_tg           | 861 ms                                                 | 582 ms: 1.48x faster                                             |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                             |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                             |
| async_tree_memoization     | 437 ms                                                 | 325 ms: 1.34x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 244 ms: 1.31x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 482 ms: 1.19x faster                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 458 ms: 1.19x faster                                             |
| async_generators           | 433 ms                                                 | 388 ms: 1.12x faster                                             |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                            |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.4 ms: 1.12x faster                                            |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                             |
| nbody          | 87.7 ms                                                | 95.4 ms: 1.09x slower                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.29 ms: 1.14x faster                                            |
| regex_dna      | 220 ms                                                 | 205 ms: 1.07x faster                                             |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                             |
| regex_v8       | 26.9 ms                                                | 25.8 ms: 1.04x faster                                            |
| Geometric mean | (ref)                                                  | 1.08x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                             |
| tomli_loads          | 2.12 sec                                               | 1.97 sec: 1.07x faster                                           |
| xml_etree_iterparse  | 101 ms                                                 | 97.5 ms: 1.04x faster                                            |
| xml_etree_generate   | 86.8 ms                                                | 84.6 ms: 1.03x faster                                            |
| xml_etree_process    | 60.5 ms                                                | 60.0 ms: 1.01x faster                                            |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                             |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                             |
| json_loads           | 27.2 us                                                | 29.5 us: 1.09x slower                                            |
| json_dumps           | 10.1 ms                                                | 12.0 ms: 1.19x slower                                            |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.04 ms: 1.00x slower                                            |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                            |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                            |
| genshi_xml      | 50.5 ms                                                | 48.0 ms: 1.05x faster                                            |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                            |
| mako            | 10.7 ms                                                | 11.5 ms: 1.08x slower                                            |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 304 ms: 1.52x faster                                             |
| async_tree_io_tg           | 861 ms                                                 | 582 ms: 1.48x faster                                             |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                             |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                             |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                             |
| async_tree_memoization     | 437 ms                                                 | 325 ms: 1.34x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 244 ms: 1.31x faster                                             |
| deepcopy_memo              | 38.4 us                                                | 30.9 us: 1.24x faster                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.65 us: 1.22x faster                                            |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 482 ms: 1.19x faster                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 458 ms: 1.19x faster                                             |
| spectral_norm              | 113 ms                                                 | 97.8 ms: 1.16x faster                                            |
| regex_effbot               | 3.77 ms                                                | 3.29 ms: 1.14x faster                                            |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                             |
| float                      | 78.7 ms                                                | 70.4 ms: 1.12x faster                                            |
| async_generators           | 433 ms                                                 | 388 ms: 1.12x faster                                             |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                             |
| pathlib                    | 17.4 ms                                                | 15.9 ms: 1.09x faster                                            |
| richards                   | 47.5 ms                                                | 43.8 ms: 1.09x faster                                            |
| telco                      | 8.40 ms                                                | 7.77 ms: 1.08x faster                                            |
| richards_super             | 53.7 ms                                                | 49.8 ms: 1.08x faster                                            |
| tomli_loads                | 2.12 sec                                               | 1.97 sec: 1.07x faster                                           |
| regex_dna                  | 220 ms                                                 | 205 ms: 1.07x faster                                             |
| gc_traversal               | 4.90 ms                                                | 4.59 ms: 1.07x faster                                            |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.76 ms: 1.06x faster                                            |
| scimark_fft                | 367 ms                                                 | 347 ms: 1.06x faster                                             |
| generators                 | 28.8 ms                                                | 27.3 ms: 1.05x faster                                            |
| genshi_xml                 | 50.5 ms                                                | 48.0 ms: 1.05x faster                                            |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                             |
| thrift                     | 800 us                                                 | 762 us: 1.05x faster                                             |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                             |
| pyflate                    | 470 ms                                                 | 449 ms: 1.05x faster                                             |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.05x faster                                           |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                            |
| crypto_pyaes               | 74.7 ms                                                | 71.6 ms: 1.04x faster                                            |
| regex_v8                   | 26.9 ms                                                | 25.8 ms: 1.04x faster                                            |
| html5lib                   | 63.4 ms                                                | 60.9 ms: 1.04x faster                                            |
| xml_etree_iterparse        | 101 ms                                                 | 97.5 ms: 1.04x faster                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.53 sec: 1.04x faster                                           |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                           |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                            |
| sqlglot_normalize          | 108 ms                                                 | 105 ms: 1.03x faster                                             |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                             |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.03x faster                                             |
| xml_etree_generate         | 86.8 ms                                                | 84.6 ms: 1.03x faster                                            |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.03x faster                                             |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                           |
| shortest_path              | 487 ms                                                 | 476 ms: 1.02x faster                                             |
| logging_simple             | 5.65 us                                                | 5.53 us: 1.02x faster                                            |
| pprint_safe_repr           | 727 ms                                                 | 712 ms: 1.02x faster                                             |
| connected_components       | 447 ms                                                 | 438 ms: 1.02x faster                                             |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                             |
| json                       | 5.32 ms                                                | 5.24 ms: 1.02x faster                                            |
| sqlglot_optimize           | 53.4 ms                                                | 52.6 ms: 1.01x faster                                            |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                             |
| logging_format             | 6.23 us                                                | 6.16 us: 1.01x faster                                            |
| sympy_expand               | 456 ms                                                 | 451 ms: 1.01x faster                                             |
| mdp                        | 2.54 sec                                               | 2.52 sec: 1.01x faster                                           |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.01x faster                                           |
| xml_etree_process          | 60.5 ms                                                | 60.0 ms: 1.01x faster                                            |
| deltablue                  | 3.19 ms                                                | 3.17 ms: 1.01x faster                                            |
| sqlglot_parse              | 1.26 ms                                                | 1.26 ms: 1.01x faster                                            |
| dulwich_log                | 64.6 ms                                                | 64.2 ms: 1.01x faster                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.56 ms: 1.01x faster                                            |
| nqueens                    | 80.9 ms                                                | 80.5 ms: 1.00x faster                                            |
| chaos                      | 58.0 ms                                                | 57.8 ms: 1.00x faster                                            |
| sympy_integrate            | 19.8 ms                                                | 19.8 ms: 1.00x faster                                            |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                             |
| docutils                   | 2.58 sec                                               | 2.59 sec: 1.00x slower                                           |
| python_startup_no_site     | 7.00 ms                                                | 7.04 ms: 1.00x slower                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 67.3 ms: 1.01x slower                                            |
| typing_runtime_protocols   | 160 us                                                 | 161 us: 1.01x slower                                             |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                             |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                            |
| fannkuch                   | 394 ms                                                 | 401 ms: 1.02x slower                                             |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                            |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                            |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                             |
| hexiom                     | 6.08 ms                                                | 6.23 ms: 1.03x slower                                            |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                             |
| bench_thread_pool          | 818 us                                                 | 865 us: 1.06x slower                                             |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                             |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                            |
| logging_silent             | 101 ns                                                 | 107 ns: 1.06x slower                                             |
| mako                       | 10.7 ms                                                | 11.5 ms: 1.08x slower                                            |
| coverage                   | 82.8 ms                                                | 89.6 ms: 1.08x slower                                            |
| json_loads                 | 27.2 us                                                | 29.5 us: 1.09x slower                                            |
| nbody                      | 87.7 ms                                                | 95.4 ms: 1.09x slower                                            |
| many_optionals             | 857 us                                                 | 942 us: 1.10x slower                                             |
| json_dumps                 | 10.1 ms                                                | 12.0 ms: 1.19x slower                                            |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.33x slower                                            |
| bench_mp_pool              | 24.0 ms                                                | 81.3 ms: 3.39x slower                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                     |

Benchmark hidden because not significant (2): create_gc_cycles, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x