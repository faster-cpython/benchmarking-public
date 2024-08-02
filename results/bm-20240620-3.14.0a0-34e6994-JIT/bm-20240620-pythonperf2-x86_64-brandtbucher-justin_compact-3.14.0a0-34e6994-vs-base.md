# Results vs. base

- fork: brandtbucher
- ref: justin_compact
- machine: linux-x86_64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.00x slower
- HPT reliability: 99.07%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                                      | 308 ms: 1.01x slower                                                        |
| html5lib       | 74.0 ms                                                                     | 73.2 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 618 ms                                                                      | 629 ms: 1.02x slower                                                        |
| async_tree_none         | 374 ms                                                                      | 383 ms: 1.02x slower                                                        |
| Geometric mean          | (ref)                                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_io, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 86.3 ms                                                                     | 82.4 ms: 1.05x faster                                                       |
| float          | 76.2 ms                                                                     | 74.4 ms: 1.02x faster                                                       |
| pidigits       | 250 ms                                                                      | 251 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 256 ms                                                                      | 240 ms: 1.06x faster                                                        |
| regex_v8       | 26.2 ms                                                                     | 25.4 ms: 1.03x faster                                                       |
| regex_compile  | 138 ms                                                                      | 139 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle             | 15.8 us                                                                     | 15.4 us: 1.03x faster                                                       |
| pickle_list          | 4.43 us                                                                     | 4.36 us: 1.02x faster                                                       |
| unpickle_pure_python | 221 us                                                                      | 218 us: 1.01x faster                                                        |
| json_dumps           | 10.7 ms                                                                     | 10.6 ms: 1.01x faster                                                       |
| tomli_loads          | 2.12 sec                                                                    | 2.11 sec: 1.01x faster                                                      |
| xml_etree_parse      | 142 ms                                                                      | 141 ms: 1.00x faster                                                        |
| pickle_dict          | 31.2 us                                                                     | 31.3 us: 1.00x slower                                                       |
| unpickle_list        | 4.71 us                                                                     | 4.74 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 98.8 ms                                                                     | 99.8 ms: 1.01x slower                                                       |
| json_loads           | 25.0 us                                                                     | 25.6 us: 1.02x slower                                                       |
| pickle               | 10.6 us                                                                     | 10.9 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 9.48 ms                                                                     | 9.50 ms: 1.00x slower                                                       |
| python_startup         | 13.8 ms                                                                     | 13.9 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 28.9 ms                                                                     | 27.3 ms: 1.06x faster                                                       |
| django_template | 42.6 ms                                                                     | 41.2 ms: 1.04x faster                                                       |
| genshi_xml      | 65.7 ms                                                                     | 63.5 ms: 1.03x faster                                                       |
| mako            | 9.27 ms                                                                     | 9.23 ms: 1.00x faster                                                       |
| Geometric mean  | (ref)                                                                       | 1.03x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|--------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coverage                 | 86.7 ms                                                                     | 79.1 ms: 1.10x faster                                                       |
| regex_dna                | 256 ms                                                                      | 240 ms: 1.06x faster                                                        |
| genshi_text              | 28.9 ms                                                                     | 27.3 ms: 1.06x faster                                                       |
| raytrace                 | 303 ms                                                                      | 287 ms: 1.06x faster                                                        |
| nbody                    | 86.3 ms                                                                     | 82.4 ms: 1.05x faster                                                       |
| chaos                    | 68.7 ms                                                                     | 66.1 ms: 1.04x faster                                                       |
| django_template          | 42.6 ms                                                                     | 41.2 ms: 1.04x faster                                                       |
| logging_silent           | 108 ns                                                                      | 104 ns: 1.03x faster                                                        |
| genshi_xml               | 65.7 ms                                                                     | 63.5 ms: 1.03x faster                                                       |
| scimark_fft              | 306 ms                                                                      | 296 ms: 1.03x faster                                                        |
| regex_v8                 | 26.2 ms                                                                     | 25.4 ms: 1.03x faster                                                       |
| unpickle                 | 15.8 us                                                                     | 15.4 us: 1.03x faster                                                       |
| scimark_sparse_mat_mult  | 4.12 ms                                                                     | 4.02 ms: 1.03x faster                                                       |
| float                    | 76.2 ms                                                                     | 74.4 ms: 1.02x faster                                                       |
| comprehensions           | 18.6 us                                                                     | 18.3 us: 1.02x faster                                                       |
| deepcopy_memo            | 29.5 us                                                                     | 29.0 us: 1.02x faster                                                       |
| bench_mp_pool            | 4.82 ms                                                                     | 4.74 ms: 1.02x faster                                                       |
| deepcopy_reduce          | 3.08 us                                                                     | 3.03 us: 1.02x faster                                                       |
| pickle_list              | 4.43 us                                                                     | 4.36 us: 1.02x faster                                                       |
| unpickle_pure_python     | 221 us                                                                      | 218 us: 1.01x faster                                                        |
| json_dumps               | 10.7 ms                                                                     | 10.6 ms: 1.01x faster                                                       |
| typing_runtime_protocols | 187 us                                                                      | 185 us: 1.01x faster                                                        |
| sympy_sum                | 166 ms                                                                      | 164 ms: 1.01x faster                                                        |
| html5lib                 | 74.0 ms                                                                     | 73.2 ms: 1.01x faster                                                       |
| asyncio_tcp              | 379 ms                                                                      | 376 ms: 1.01x faster                                                        |
| tomli_loads              | 2.12 sec                                                                    | 2.11 sec: 1.01x faster                                                      |
| pyflate                  | 452 ms                                                                      | 449 ms: 1.01x faster                                                        |
| sympy_integrate          | 25.6 ms                                                                     | 25.5 ms: 1.01x faster                                                       |
| mdp                      | 2.60 sec                                                                    | 2.59 sec: 1.00x faster                                                      |
| mako                     | 9.27 ms                                                                     | 9.23 ms: 1.00x faster                                                       |
| xml_etree_parse          | 142 ms                                                                      | 141 ms: 1.00x faster                                                        |
| pathlib                  | 16.2 ms                                                                     | 16.2 ms: 1.00x faster                                                       |
| create_gc_cycles         | 1.91 ms                                                                     | 1.91 ms: 1.00x faster                                                       |
| hexiom                   | 6.77 ms                                                                     | 6.75 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl          | 1.58 sec                                                                    | 1.58 sec: 1.00x slower                                                      |
| python_startup_no_site   | 9.48 ms                                                                     | 9.50 ms: 1.00x slower                                                       |
| python_startup           | 13.8 ms                                                                     | 13.9 ms: 1.00x slower                                                       |
| pidigits                 | 250 ms                                                                      | 251 ms: 1.00x slower                                                        |
| generators               | 34.0 ms                                                                     | 34.1 ms: 1.00x slower                                                       |
| pickle_dict              | 31.2 us                                                                     | 31.3 us: 1.00x slower                                                       |
| sqlite_synth             | 2.77 us                                                                     | 2.78 us: 1.01x slower                                                       |
| bpe_tokeniser            | 5.18 sec                                                                    | 5.21 sec: 1.01x slower                                                      |
| unpickle_list            | 4.71 us                                                                     | 4.74 us: 1.01x slower                                                       |
| regex_compile            | 138 ms                                                                      | 139 ms: 1.01x slower                                                        |
| pprint_safe_repr         | 787 ms                                                                      | 793 ms: 1.01x slower                                                        |
| scimark_lu               | 114 ms                                                                      | 115 ms: 1.01x slower                                                        |
| async_generators         | 386 ms                                                                      | 389 ms: 1.01x slower                                                        |
| sympy_expand             | 528 ms                                                                      | 533 ms: 1.01x slower                                                        |
| scimark_monte_carlo      | 66.8 ms                                                                     | 67.4 ms: 1.01x slower                                                       |
| xml_etree_iterparse      | 98.8 ms                                                                     | 99.8 ms: 1.01x slower                                                       |
| sqlglot_normalize        | 130 ms                                                                      | 131 ms: 1.01x slower                                                        |
| sqlglot_transpile        | 1.83 ms                                                                     | 1.85 ms: 1.01x slower                                                       |
| 2to3                     | 304 ms                                                                      | 308 ms: 1.01x slower                                                        |
| go                       | 163 ms                                                                      | 165 ms: 1.01x slower                                                        |
| gc_traversal             | 4.36 ms                                                                     | 4.42 ms: 1.01x slower                                                       |
| richards                 | 46.2 ms                                                                     | 46.9 ms: 1.02x slower                                                       |
| coroutines               | 21.9 ms                                                                     | 22.2 ms: 1.02x slower                                                       |
| dulwich_log              | 66.0 ms                                                                     | 67.1 ms: 1.02x slower                                                       |
| telco                    | 8.07 ms                                                                     | 8.22 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed  | 618 ms                                                                      | 629 ms: 1.02x slower                                                        |
| nqueens                  | 94.3 ms                                                                     | 96.2 ms: 1.02x slower                                                       |
| sqlglot_optimize         | 63.1 ms                                                                     | 64.4 ms: 1.02x slower                                                       |
| dask                     | 399 ms                                                                      | 407 ms: 1.02x slower                                                        |
| meteor_contest           | 128 ms                                                                      | 130 ms: 1.02x slower                                                        |
| sqlglot_parse            | 1.42 ms                                                                     | 1.45 ms: 1.02x slower                                                       |
| async_tree_none          | 374 ms                                                                      | 383 ms: 1.02x slower                                                        |
| json_loads               | 25.0 us                                                                     | 25.6 us: 1.02x slower                                                       |
| richards_super           | 53.1 ms                                                                     | 54.5 ms: 1.03x slower                                                       |
| pycparser                | 1.25 sec                                                                    | 1.28 sec: 1.03x slower                                                      |
| crypto_pyaes             | 70.0 ms                                                                     | 72.0 ms: 1.03x slower                                                       |
| pickle                   | 10.6 us                                                                     | 10.9 us: 1.03x slower                                                       |
| thrift                   | 897 us                                                                      | 924 us: 1.03x slower                                                        |
| json                     | 5.35 ms                                                                     | 5.52 ms: 1.03x slower                                                       |
| logging_format           | 6.84 us                                                                     | 7.06 us: 1.03x slower                                                       |
| logging_simple           | 6.17 us                                                                     | 6.43 us: 1.04x slower                                                       |
| bench_thread_pool        | 926 us                                                                      | 975 us: 1.05x slower                                                        |
| scimark_sor              | 125 ms                                                                      | 137 ms: 1.09x slower                                                        |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (20): spectral_norm, xml_etree_process, xml_etree_generate, regex_effbot, fannkuch, pickle_pure_python, asyncio_websockets, docutils, pprint_pformat, sympy_str, pylint, deltablue, async_tree_io_tg, tornado_http, deepcopy, async_tree_io, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg

# HPT report

- Reliability score: 99.07% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x