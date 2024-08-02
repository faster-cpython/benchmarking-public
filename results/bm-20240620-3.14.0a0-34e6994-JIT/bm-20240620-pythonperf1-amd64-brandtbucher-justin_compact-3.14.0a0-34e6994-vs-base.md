# Results vs. base

- fork: brandtbucher
- ref: justin_compact
- machine: windows-amd64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.01x faster
- HPT reliability: 82.40%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 231 ms                                                                     | 228 ms: 1.01x faster                                                       |
| docutils       | 1.74 sec                                                                   | 1.73 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 53.2 ms                                                                    | 50.6 ms: 1.05x faster                                                      |
| pidigits       | 149 ms                                                                     | 150 ms: 1.01x slower                                                       |
| float          | 44.2 ms                                                                    | 44.5 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.1 ms                                                                    | 82.2 ms: 1.06x faster                                                      |
| regex_dna      | 119 ms                                                                     | 116 ms: 1.02x faster                                                       |
| regex_effbot   | 1.57 ms                                                                    | 1.55 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.05x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle             | 9.11 us                                                                    | 8.70 us: 1.05x faster                                                      |
| xml_etree_parse      | 95.8 ms                                                                    | 92.2 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 61.2 ms                                                                    | 59.7 ms: 1.02x faster                                                      |
| tomli_loads          | 1.20 sec                                                                   | 1.18 sec: 1.01x faster                                                     |
| xml_etree_generate   | 51.0 ms                                                                    | 50.4 ms: 1.01x faster                                                      |
| unpickle_pure_python | 124 us                                                                     | 123 us: 1.01x faster                                                       |
| pickle_dict          | 17.5 us                                                                    | 17.6 us: 1.00x slower                                                      |
| json_loads           | 13.9 us                                                                    | 14.1 us: 1.02x slower                                                      |
| json_dumps           | 5.56 ms                                                                    | 5.70 ms: 1.03x slower                                                      |
| pickle               | 7.18 us                                                                    | 7.49 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_process, unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 42.4 ms                                                                    | 37.9 ms: 1.12x faster                                                      |
| genshi_text     | 17.0 ms                                                                    | 16.4 ms: 1.04x faster                                                      |
| django_template | 24.7 ms                                                                    | 24.0 ms: 1.03x faster                                                      |
| Geometric mean  | (ref)                                                                      | 1.04x faster                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|--------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| hexiom                   | 4.65 ms                                                                    | 4.12 ms: 1.13x faster                                                      |
| genshi_xml               | 42.4 ms                                                                    | 37.9 ms: 1.12x faster                                                      |
| scimark_lu               | 74.3 ms                                                                    | 67.7 ms: 1.10x faster                                                      |
| regex_compile            | 87.1 ms                                                                    | 82.2 ms: 1.06x faster                                                      |
| nqueens                  | 60.6 ms                                                                    | 57.2 ms: 1.06x faster                                                      |
| nbody                    | 53.2 ms                                                                    | 50.6 ms: 1.05x faster                                                      |
| unpickle                 | 9.11 us                                                                    | 8.70 us: 1.05x faster                                                      |
| go                       | 90.3 ms                                                                    | 86.7 ms: 1.04x faster                                                      |
| genshi_text              | 17.0 ms                                                                    | 16.4 ms: 1.04x faster                                                      |
| xml_etree_parse          | 95.8 ms                                                                    | 92.2 ms: 1.04x faster                                                      |
| generators               | 20.3 ms                                                                    | 19.7 ms: 1.03x faster                                                      |
| django_template          | 24.7 ms                                                                    | 24.0 ms: 1.03x faster                                                      |
| deltablue                | 2.13 ms                                                                    | 2.07 ms: 1.03x faster                                                      |
| xml_etree_iterparse      | 61.2 ms                                                                    | 59.7 ms: 1.02x faster                                                      |
| regex_dna                | 119 ms                                                                     | 116 ms: 1.02x faster                                                       |
| scimark_sor              | 84.8 ms                                                                    | 83.0 ms: 1.02x faster                                                      |
| sympy_sum                | 91.8 ms                                                                    | 90.1 ms: 1.02x faster                                                      |
| telco                    | 4.57 ms                                                                    | 4.49 ms: 1.02x faster                                                      |
| pyflate                  | 257 ms                                                                     | 253 ms: 1.02x faster                                                       |
| tomli_loads              | 1.20 sec                                                                   | 1.18 sec: 1.01x faster                                                     |
| richards_super           | 34.4 ms                                                                    | 33.9 ms: 1.01x faster                                                      |
| sympy_str                | 176 ms                                                                     | 173 ms: 1.01x faster                                                       |
| regex_effbot             | 1.57 ms                                                                    | 1.55 ms: 1.01x faster                                                      |
| 2to3                     | 231 ms                                                                     | 228 ms: 1.01x faster                                                       |
| richards                 | 30.4 ms                                                                    | 30.0 ms: 1.01x faster                                                      |
| xml_etree_generate       | 51.0 ms                                                                    | 50.4 ms: 1.01x faster                                                      |
| sympy_expand             | 305 ms                                                                     | 301 ms: 1.01x faster                                                       |
| comprehensions           | 10.2 us                                                                    | 10.1 us: 1.01x faster                                                      |
| sqlglot_optimize         | 35.4 ms                                                                    | 35.0 ms: 1.01x faster                                                      |
| fannkuch                 | 223 ms                                                                     | 220 ms: 1.01x faster                                                       |
| sqlglot_transpile        | 1.00 ms                                                                    | 991 us: 1.01x faster                                                       |
| meteor_contest           | 72.9 ms                                                                    | 72.3 ms: 1.01x faster                                                      |
| logging_format           | 5.98 us                                                                    | 5.94 us: 1.01x faster                                                      |
| docutils                 | 1.74 sec                                                                   | 1.73 sec: 1.01x faster                                                     |
| unpickle_pure_python     | 124 us                                                                     | 123 us: 1.01x faster                                                       |
| chaos                    | 38.5 ms                                                                    | 38.3 ms: 1.01x faster                                                      |
| async_generators         | 252 ms                                                                     | 250 ms: 1.01x faster                                                       |
| sqlite_synth             | 1.58 us                                                                    | 1.58 us: 1.00x faster                                                      |
| spectral_norm            | 45.0 ms                                                                    | 45.1 ms: 1.00x slower                                                      |
| pickle_dict              | 17.5 us                                                                    | 17.6 us: 1.00x slower                                                      |
| pidigits                 | 149 ms                                                                     | 150 ms: 1.01x slower                                                       |
| float                    | 44.2 ms                                                                    | 44.5 ms: 1.01x slower                                                      |
| scimark_monte_carlo      | 37.1 ms                                                                    | 37.4 ms: 1.01x slower                                                      |
| coverage                 | 44.0 ms                                                                    | 44.4 ms: 1.01x slower                                                      |
| sqlglot_parse            | 773 us                                                                     | 781 us: 1.01x slower                                                       |
| crypto_pyaes             | 40.7 ms                                                                    | 41.1 ms: 1.01x slower                                                      |
| bench_mp_pool            | 69.6 ms                                                                    | 70.6 ms: 1.02x slower                                                      |
| json_loads               | 13.9 us                                                                    | 14.1 us: 1.02x slower                                                      |
| json                     | 2.89 ms                                                                    | 2.94 ms: 1.02x slower                                                      |
| coroutines               | 12.7 ms                                                                    | 12.9 ms: 1.02x slower                                                      |
| typing_runtime_protocols | 109 us                                                                     | 111 us: 1.02x slower                                                       |
| pprint_safe_repr         | 452 ms                                                                     | 460 ms: 1.02x slower                                                       |
| thrift                   | 492 us                                                                     | 505 us: 1.03x slower                                                       |
| json_dumps               | 5.56 ms                                                                    | 5.70 ms: 1.03x slower                                                      |
| mdp                      | 1.37 sec                                                                   | 1.40 sec: 1.03x slower                                                     |
| logging_silent           | 53.1 ns                                                                    | 54.7 ns: 1.03x slower                                                      |
| deepcopy_memo            | 15.1 us                                                                    | 15.6 us: 1.03x slower                                                      |
| scimark_fft              | 149 ms                                                                     | 154 ms: 1.03x slower                                                       |
| pickle                   | 7.18 us                                                                    | 7.49 us: 1.04x slower                                                      |
| scimark_sparse_mat_mult  | 2.09 ms                                                                    | 2.21 ms: 1.06x slower                                                      |
| Geometric mean           | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (32): regex_v8, pycparser, pylint, deepcopy, deepcopy_reduce, create_gc_cycles, async_tree_memoization_tg, sympy_integrate, tornado_http, pickle_pure_python, logging_simple, python_startup, pprint_pformat, asyncio_tcp, bench_thread_pool, python_startup_no_site, raytrace, pathlib, html5lib, gc_traversal, xml_etree_process, mako, unpickle_list, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg, async_tree_none_tg, pickle_list, async_tree_none, asyncio_tcp_ssl

# HPT report

- Reliability score: 82.40% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown