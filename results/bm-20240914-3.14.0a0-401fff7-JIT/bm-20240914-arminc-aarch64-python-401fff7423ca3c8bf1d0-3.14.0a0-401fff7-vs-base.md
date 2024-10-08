# Results vs. base

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-aarch64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.12x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 295 ms                                                                                                            | 380 ms: 1.29x slower                                                                                                  |
| docutils       | 3.01 sec                                                                                                          | 3.98 sec: 1.32x slower                                                                                                |
| html5lib       | 65.5 ms                                                                                                           | 71.3 ms: 1.09x slower                                                                                                 |
| tornado_http   | 128 ms                                                                                                            | 147 ms: 1.15x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.21x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.22 sec                                                                                                          | 2.25 sec: 1.01x slower                                                                                                |
| async_tree_memoization_tg  | 555 ms                                                                                                            | 564 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 728 ms                                                                                                            | 742 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 737 ms                                                                                                            | 757 ms: 1.03x slower                                                                                                  |
| async_generators           | 483 ms                                                                                                            | 501 ms: 1.04x slower                                                                                                  |
| async_tree_none            | 424 ms                                                                                                            | 444 ms: 1.05x slower                                                                                                  |
| async_tree_memoization     | 558 ms                                                                                                            | 588 ms: 1.05x slower                                                                                                  |
| asyncio_tcp                | 576 ms                                                                                                            | 619 ms: 1.07x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (5): async_tree_io_tg, coroutines, asyncio_websockets, async_tree_io, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 92.7 ms                                                                                                           | 87.5 ms: 1.06x faster                                                                                                 |
| nbody          | 110 ms                                                                                                            | 114 ms: 1.03x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                                                                            | 242 ms: 1.03x faster                                                                                                  |
| regex_v8       | 30.3 ms                                                                                                           | 31.5 ms: 1.04x slower                                                                                                 |
| regex_compile  | 126 ms                                                                                                            | 190 ms: 1.51x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.11x slower                                                                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| xml_etree_generate   | 112 ms                                                                                                            | 111 ms: 1.01x faster                                                                                                  |
| pickle_dict          | 37.6 us                                                                                                           | 38.2 us: 1.02x slower                                                                                                 |
| pickle               | 13.5 us                                                                                                           | 13.8 us: 1.02x slower                                                                                                 |
| json_dumps           | 13.2 ms                                                                                                           | 13.5 ms: 1.02x slower                                                                                                 |
| pickle_pure_python   | 362 us                                                                                                            | 380 us: 1.05x slower                                                                                                  |
| unpickle_pure_python | 252 us                                                                                                            | 267 us: 1.06x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (8): json_loads, xml_etree_parse, tomli_loads, unpickle_list, unpickle, xml_etree_process, pickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                                                           | 13.0 ms: 1.01x slower                                                                                                 |
| python_startup_no_site | 8.62 ms                                                                                                           | 8.80 ms: 1.02x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.5 ms                                                                                                           | 13.1 ms: 1.04x faster                                                                                                 |
| django_template | 41.7 ms                                                                                                           | 50.8 ms: 1.22x slower                                                                                                 |
| genshi_text     | 27.5 ms                                                                                                           | 35.7 ms: 1.29x slower                                                                                                 |
| genshi_xml      | 60.4 ms                                                                                                           | 82.2 ms: 1.36x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.20x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                  | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float                      | 92.7 ms                                                                                                           | 87.5 ms: 1.06x faster                                                                                                 |
| mako                       | 13.5 ms                                                                                                           | 13.1 ms: 1.04x faster                                                                                                 |
| scimark_sor                | 157 ms                                                                                                            | 152 ms: 1.04x faster                                                                                                  |
| regex_dna                  | 249 ms                                                                                                            | 242 ms: 1.03x faster                                                                                                  |
| deepcopy_memo              | 37.7 us                                                                                                           | 37.2 us: 1.01x faster                                                                                                 |
| xml_etree_generate         | 112 ms                                                                                                            | 111 ms: 1.01x faster                                                                                                  |
| python_startup             | 12.9 ms                                                                                                           | 13.0 ms: 1.01x slower                                                                                                 |
| asyncio_tcp_ssl            | 2.22 sec                                                                                                          | 2.25 sec: 1.01x slower                                                                                                |
| bpe_tokeniser              | 5.86 sec                                                                                                          | 5.94 sec: 1.01x slower                                                                                                |
| async_tree_memoization_tg  | 555 ms                                                                                                            | 564 ms: 1.02x slower                                                                                                  |
| pickle_dict                | 37.6 us                                                                                                           | 38.2 us: 1.02x slower                                                                                                 |
| pickle                     | 13.5 us                                                                                                           | 13.8 us: 1.02x slower                                                                                                 |
| async_tree_cpu_io_mixed_tg | 728 ms                                                                                                            | 742 ms: 1.02x slower                                                                                                  |
| json_dumps                 | 13.2 ms                                                                                                           | 13.5 ms: 1.02x slower                                                                                                 |
| sqlite_synth               | 3.81 us                                                                                                           | 3.88 us: 1.02x slower                                                                                                 |
| python_startup_no_site     | 8.62 ms                                                                                                           | 8.80 ms: 1.02x slower                                                                                                 |
| async_tree_cpu_io_mixed    | 737 ms                                                                                                            | 757 ms: 1.03x slower                                                                                                  |
| json                       | 5.57 ms                                                                                                           | 5.73 ms: 1.03x slower                                                                                                 |
| coverage                   | 97.5 ms                                                                                                           | 101 ms: 1.03x slower                                                                                                  |
| nbody                      | 110 ms                                                                                                            | 114 ms: 1.03x slower                                                                                                  |
| scimark_fft                | 442 ms                                                                                                            | 459 ms: 1.04x slower                                                                                                  |
| pathlib                    | 20.7 ms                                                                                                           | 21.5 ms: 1.04x slower                                                                                                 |
| spectral_norm              | 140 ms                                                                                                            | 145 ms: 1.04x slower                                                                                                  |
| async_generators           | 483 ms                                                                                                            | 501 ms: 1.04x slower                                                                                                  |
| regex_v8                   | 30.3 ms                                                                                                           | 31.5 ms: 1.04x slower                                                                                                 |
| async_tree_none            | 424 ms                                                                                                            | 444 ms: 1.05x slower                                                                                                  |
| pickle_pure_python         | 362 us                                                                                                            | 380 us: 1.05x slower                                                                                                  |
| mdp                        | 3.33 sec                                                                                                          | 3.50 sec: 1.05x slower                                                                                                |
| logging_silent             | 133 ns                                                                                                            | 140 ns: 1.05x slower                                                                                                  |
| async_tree_memoization     | 558 ms                                                                                                            | 588 ms: 1.05x slower                                                                                                  |
| thrift                     | 931 us                                                                                                            | 981 us: 1.05x slower                                                                                                  |
| unpickle_pure_python       | 252 us                                                                                                            | 267 us: 1.06x slower                                                                                                  |
| telco                      | 9.86 ms                                                                                                           | 10.5 ms: 1.06x slower                                                                                                 |
| scimark_sparse_mat_mult    | 6.42 ms                                                                                                           | 6.82 ms: 1.06x slower                                                                                                 |
| logging_simple             | 7.01 us                                                                                                           | 7.52 us: 1.07x slower                                                                                                 |
| asyncio_tcp                | 576 ms                                                                                                            | 619 ms: 1.07x slower                                                                                                  |
| logging_format             | 7.63 us                                                                                                           | 8.20 us: 1.07x slower                                                                                                 |
| typing_runtime_protocols   | 193 us                                                                                                            | 207 us: 1.08x slower                                                                                                  |
| bench_mp_pool              | 7.01 ms                                                                                                           | 7.57 ms: 1.08x slower                                                                                                 |
| html5lib                   | 65.5 ms                                                                                                           | 71.3 ms: 1.09x slower                                                                                                 |
| fannkuch                   | 460 ms                                                                                                            | 503 ms: 1.09x slower                                                                                                  |
| deepcopy_reduce            | 3.52 us                                                                                                           | 3.86 us: 1.10x slower                                                                                                 |
| crypto_pyaes               | 81.3 ms                                                                                                           | 89.4 ms: 1.10x slower                                                                                                 |
| bench_thread_pool          | 1.23 ms                                                                                                           | 1.36 ms: 1.10x slower                                                                                                 |
| scimark_lu                 | 135 ms                                                                                                            | 149 ms: 1.10x slower                                                                                                  |
| deltablue                  | 3.92 ms                                                                                                           | 4.36 ms: 1.11x slower                                                                                                 |
| meteor_contest             | 111 ms                                                                                                            | 124 ms: 1.12x slower                                                                                                  |
| scimark_monte_carlo        | 82.5 ms                                                                                                           | 92.5 ms: 1.12x slower                                                                                                 |
| tornado_http               | 128 ms                                                                                                            | 147 ms: 1.15x slower                                                                                                  |
| raytrace                   | 303 ms                                                                                                            | 350 ms: 1.16x slower                                                                                                  |
| pyflate                    | 562 ms                                                                                                            | 654 ms: 1.16x slower                                                                                                  |
| deepcopy                   | 334 us                                                                                                            | 394 us: 1.18x slower                                                                                                  |
| sqlglot_normalize          | 127 ms                                                                                                            | 151 ms: 1.19x slower                                                                                                  |
| comprehensions             | 20.6 us                                                                                                           | 24.5 us: 1.19x slower                                                                                                 |
| django_template            | 41.7 ms                                                                                                           | 50.8 ms: 1.22x slower                                                                                                 |
| richards                   | 52.7 ms                                                                                                           | 66.3 ms: 1.26x slower                                                                                                 |
| sqlglot_parse              | 1.40 ms                                                                                                           | 1.77 ms: 1.27x slower                                                                                                 |
| sqlglot_optimize           | 62.3 ms                                                                                                           | 78.9 ms: 1.27x slower                                                                                                 |
| pycparser                  | 1.22 sec                                                                                                          | 1.54 sec: 1.27x slower                                                                                                |
| richards_super             | 59.4 ms                                                                                                           | 75.3 ms: 1.27x slower                                                                                                 |
| sqlglot_transpile          | 1.74 ms                                                                                                           | 2.21 ms: 1.27x slower                                                                                                 |
| nqueens                    | 101 ms                                                                                                            | 128 ms: 1.27x slower                                                                                                  |
| 2to3                       | 295 ms                                                                                                            | 380 ms: 1.29x slower                                                                                                  |
| genshi_text                | 27.5 ms                                                                                                           | 35.7 ms: 1.29x slower                                                                                                 |
| pylint                     | 359 ms                                                                                                            | 473 ms: 1.32x slower                                                                                                  |
| docutils                   | 3.01 sec                                                                                                          | 3.98 sec: 1.32x slower                                                                                                |
| chaos                      | 69.0 ms                                                                                                           | 92.1 ms: 1.33x slower                                                                                                 |
| go                         | 139 ms                                                                                                            | 186 ms: 1.34x slower                                                                                                  |
| sympy_expand               | 460 ms                                                                                                            | 618 ms: 1.34x slower                                                                                                  |
| pprint_safe_repr           | 926 ms                                                                                                            | 1.25 sec: 1.35x slower                                                                                                |
| genshi_xml                 | 60.4 ms                                                                                                           | 82.2 ms: 1.36x slower                                                                                                 |
| pprint_pformat             | 1.91 sec                                                                                                          | 2.60 sec: 1.37x slower                                                                                                |
| dulwich_log                | 58.3 ms                                                                                                           | 80.8 ms: 1.39x slower                                                                                                 |
| sympy_integrate            | 20.8 ms                                                                                                           | 29.0 ms: 1.39x slower                                                                                                 |
| sympy_str                  | 264 ms                                                                                                            | 368 ms: 1.39x slower                                                                                                  |
| hexiom                     | 7.10 ms                                                                                                           | 10.2 ms: 1.44x slower                                                                                                 |
| regex_compile              | 126 ms                                                                                                            | 190 ms: 1.51x slower                                                                                                  |
| sympy_sum                  | 142 ms                                                                                                            | 216 ms: 1.53x slower                                                                                                  |
| generators                 | 34.7 ms                                                                                                           | 57.4 ms: 1.65x slower                                                                                                 |
| unpack_sequence            | 59.0 ns                                                                                                           | 146 ns: 2.48x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.12x slower                                                                                                          |

Benchmark hidden because not significant (17): create_gc_cycles, async_tree_io_tg, gc_traversal, json_loads, regex_effbot, coroutines, xml_etree_parse, tomli_loads, pidigits, unpickle_list, unpickle, asyncio_websockets, async_tree_io, xml_etree_process, pickle_list, xml_etree_iterparse, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.09x