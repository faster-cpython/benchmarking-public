# Results vs. 3.13.0b2

- fork: diegorusso
- ref: gh_119726_trampoline
- machine: linux-aarch64
- commit hash: cebe632
- commit date: 2024-06-25
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 364 ms: 1.19x slower                                                        |
| docutils       | 3.10 sec                                                     | 3.53 sec: 1.14x slower                                                      |
| html5lib       | 66.1 ms                                                      | 70.5 ms: 1.07x slower                                                       |
| tornado_http   | 128 ms                                                       | 140 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.12x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 411 ms: 1.16x faster                                                        |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.15x faster                                                      |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.15x faster                                                      |
| async_tree_memoization_tg  | 604 ms                                                       | 538 ms: 1.12x faster                                                        |
| async_tree_memoization     | 645 ms                                                       | 582 ms: 1.11x faster                                                        |
| async_tree_none            | 492 ms                                                       | 452 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 739 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 723 ms: 1.06x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 88.7 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 251 ms: 1.03x faster                                                        |
| regex_effbot   | 4.98 ms                                                      | 4.87 ms: 1.02x faster                                                       |
| regex_v8       | 31.1 ms                                                      | 30.4 ms: 1.02x faster                                                       |
| regex_compile  | 128 ms                                                       | 173 ms: 1.35x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 110 ms: 1.03x faster                                                        |
| xml_etree_process    | 80.8 ms                                                      | 78.9 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 147 ms                                                       | 147 ms: 1.00x slower                                                        |
| unpickle             | 19.8 us                                                      | 19.9 us: 1.01x slower                                                       |
| unpickle_list        | 6.52 us                                                      | 6.67 us: 1.02x slower                                                       |
| json_dumps           | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                       |
| json_loads           | 32.1 us                                                      | 33.1 us: 1.03x slower                                                       |
| tomli_loads          | 2.57 sec                                                     | 2.68 sec: 1.04x slower                                                      |
| pickle               | 13.4 us                                                      | 14.0 us: 1.05x slower                                                       |
| pickle_pure_python   | 359 us                                                       | 396 us: 1.11x slower                                                        |
| unpickle_pure_python | 251 us                                                       | 279 us: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (3): xml_etree_parse, pickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 15.4 ms: 1.19x slower                                                       |
| python_startup_no_site | 8.60 ms                                                      | 11.1 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 13.2 ms: 1.00x slower                                                       |
| django_template | 42.3 ms                                                      | 50.2 ms: 1.19x slower                                                       |
| genshi_text     | 27.4 ms                                                      | 35.1 ms: 1.28x slower                                                       |
| genshi_xml      | 60.4 ms                                                      | 82.6 ms: 1.37x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.20x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.9 us: 1.30x faster                                                       |
| deepcopy                   | 448 us                                                       | 386 us: 1.16x faster                                                        |
| async_tree_none_tg         | 476 ms                                                       | 411 ms: 1.16x faster                                                        |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.15x faster                                                      |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.15x faster                                                      |
| async_tree_memoization_tg  | 604 ms                                                       | 538 ms: 1.12x faster                                                        |
| async_tree_memoization     | 645 ms                                                       | 582 ms: 1.11x faster                                                        |
| async_tree_none            | 492 ms                                                       | 452 ms: 1.09x faster                                                        |
| gc_traversal               | 5.17 ms                                                      | 4.82 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 739 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 723 ms: 1.06x faster                                                        |
| regex_dna                  | 259 ms                                                       | 251 ms: 1.03x faster                                                        |
| float                      | 91.4 ms                                                      | 88.7 ms: 1.03x faster                                                       |
| xml_etree_generate         | 114 ms                                                       | 110 ms: 1.03x faster                                                        |
| xml_etree_process          | 80.8 ms                                                      | 78.9 ms: 1.02x faster                                                       |
| regex_effbot               | 4.98 ms                                                      | 4.87 ms: 1.02x faster                                                       |
| regex_v8                   | 31.1 ms                                                      | 30.4 ms: 1.02x faster                                                       |
| mako                       | 13.2 ms                                                      | 13.2 ms: 1.00x slower                                                       |
| xml_etree_iterparse        | 147 ms                                                       | 147 ms: 1.00x slower                                                        |
| unpickle                   | 19.8 us                                                      | 19.9 us: 1.01x slower                                                       |
| meteor_contest             | 113 ms                                                       | 115 ms: 1.01x slower                                                        |
| asyncio_websockets         | 657 ms                                                       | 665 ms: 1.01x slower                                                        |
| telco                      | 10.0 ms                                                      | 10.1 ms: 1.01x slower                                                       |
| coroutines                 | 29.0 ms                                                      | 29.5 ms: 1.02x slower                                                       |
| logging_format             | 7.82 us                                                      | 8.01 us: 1.02x slower                                                       |
| unpickle_list              | 6.52 us                                                      | 6.67 us: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.71 ms: 1.02x slower                                                       |
| fannkuch                   | 451 ms                                                       | 464 ms: 1.03x slower                                                        |
| json_dumps                 | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                       |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.28 sec: 1.03x slower                                                      |
| json_loads                 | 32.1 us                                                      | 33.1 us: 1.03x slower                                                       |
| bpe_tokeniser              | 5.83 sec                                                     | 6.01 sec: 1.03x slower                                                      |
| json                       | 5.64 ms                                                      | 5.82 ms: 1.03x slower                                                       |
| deepcopy_reduce            | 4.04 us                                                      | 4.17 us: 1.03x slower                                                       |
| spectral_norm              | 141 ms                                                       | 146 ms: 1.04x slower                                                        |
| dask                       | 370 ms                                                       | 385 ms: 1.04x slower                                                        |
| async_generators           | 488 ms                                                       | 507 ms: 1.04x slower                                                        |
| scimark_fft                | 445 ms                                                       | 463 ms: 1.04x slower                                                        |
| tomli_loads                | 2.57 sec                                                     | 2.68 sec: 1.04x slower                                                      |
| logging_silent             | 133 ns                                                       | 139 ns: 1.04x slower                                                        |
| generators                 | 37.1 ms                                                      | 38.8 ms: 1.04x slower                                                       |
| crypto_pyaes               | 82.0 ms                                                      | 85.8 ms: 1.05x slower                                                       |
| pickle                     | 13.4 us                                                      | 14.0 us: 1.05x slower                                                       |
| mdp                        | 3.33 sec                                                     | 3.49 sec: 1.05x slower                                                      |
| coverage                   | 98.4 ms                                                      | 103 ms: 1.05x slower                                                        |
| scimark_monte_carlo        | 82.3 ms                                                      | 87.5 ms: 1.06x slower                                                       |
| html5lib                   | 66.1 ms                                                      | 70.5 ms: 1.07x slower                                                       |
| typing_runtime_protocols   | 193 us                                                       | 207 us: 1.07x slower                                                        |
| bench_thread_pool          | 1.26 ms                                                      | 1.35 ms: 1.07x slower                                                       |
| scimark_sor                | 159 ms                                                       | 174 ms: 1.09x slower                                                        |
| pycparser                  | 1.22 sec                                                     | 1.34 sec: 1.10x slower                                                      |
| tornado_http               | 128 ms                                                       | 140 ms: 1.10x slower                                                        |
| raytrace                   | 297 ms                                                       | 325 ms: 1.10x slower                                                        |
| pickle_pure_python         | 359 us                                                       | 396 us: 1.11x slower                                                        |
| go                         | 161 ms                                                       | 178 ms: 1.11x slower                                                        |
| asyncio_tcp                | 584 ms                                                       | 647 ms: 1.11x slower                                                        |
| unpickle_pure_python       | 251 us                                                       | 279 us: 1.11x slower                                                        |
| sqlglot_optimize           | 62.6 ms                                                      | 69.5 ms: 1.11x slower                                                       |
| sqlglot_normalize          | 129 ms                                                       | 144 ms: 1.11x slower                                                        |
| pyflate                    | 557 ms                                                       | 619 ms: 1.11x slower                                                        |
| bench_mp_pool              | 7.03 ms                                                      | 7.88 ms: 1.12x slower                                                       |
| docutils                   | 3.10 sec                                                     | 3.53 sec: 1.14x slower                                                      |
| comprehensions             | 20.5 us                                                      | 23.5 us: 1.15x slower                                                       |
| sqlglot_parse              | 1.42 ms                                                      | 1.64 ms: 1.15x slower                                                       |
| deltablue                  | 3.88 ms                                                      | 4.47 ms: 1.15x slower                                                       |
| dulwich_log                | 58.5 ms                                                      | 68.7 ms: 1.17x slower                                                       |
| sympy_expand               | 457 ms                                                       | 537 ms: 1.17x slower                                                        |
| sqlglot_transpile          | 1.71 ms                                                      | 2.02 ms: 1.18x slower                                                       |
| django_template            | 42.3 ms                                                      | 50.2 ms: 1.19x slower                                                       |
| python_startup             | 13.0 ms                                                      | 15.4 ms: 1.19x slower                                                       |
| 2to3                       | 305 ms                                                       | 364 ms: 1.19x slower                                                        |
| nqueens                    | 98.9 ms                                                      | 119 ms: 1.20x slower                                                        |
| sympy_str                  | 265 ms                                                       | 319 ms: 1.20x slower                                                        |
| pprint_safe_repr           | 933 ms                                                       | 1.14 sec: 1.22x slower                                                      |
| pprint_pformat             | 1.93 sec                                                     | 2.38 sec: 1.23x slower                                                      |
| sympy_integrate            | 20.9 ms                                                      | 26.2 ms: 1.26x slower                                                       |
| pylint                     | 337 ms                                                       | 424 ms: 1.26x slower                                                        |
| hexiom                     | 7.08 ms                                                      | 8.97 ms: 1.27x slower                                                       |
| sympy_sum                  | 144 ms                                                       | 183 ms: 1.27x slower                                                        |
| scimark_lu                 | 141 ms                                                       | 181 ms: 1.28x slower                                                        |
| genshi_text                | 27.4 ms                                                      | 35.1 ms: 1.28x slower                                                       |
| chaos                      | 68.3 ms                                                      | 88.1 ms: 1.29x slower                                                       |
| python_startup_no_site     | 8.60 ms                                                      | 11.1 ms: 1.29x slower                                                       |
| regex_compile              | 128 ms                                                       | 173 ms: 1.35x slower                                                        |
| genshi_xml                 | 60.4 ms                                                      | 82.6 ms: 1.37x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                                |

Benchmark hidden because not significant (12): xml_etree_parse, pathlib, sqlite_synth, create_gc_cycles, logging_simple, pidigits, richards, nbody, pickle_list, pickle_dict, thrift, richards_super
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.10x