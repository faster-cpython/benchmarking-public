# Results vs. base

- fork: brandtbucher
- ref: no_cold_exits
- machine: windows-amd64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.00x faster
- HPT reliability: 90.33%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| html5lib       | 36.8 ms                                                                    | 37.2 ms: 1.01x slower                                                     |
| tornado_http   | 86.2 ms                                                                    | 85.5 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                              |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io, async_tree_none, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 149 ms                                                                     | 150 ms: 1.01x slower                                                      |
| nbody          | 53.1 ms                                                                    | 56.2 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                                     | 116 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                              |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 5.75 ms                                                                    | 5.62 ms: 1.02x faster                                                     |
| pickle_dict          | 17.8 us                                                                    | 17.6 us: 1.01x faster                                                     |
| unpickle_pure_python | 129 us                                                                     | 128 us: 1.01x faster                                                      |
| pickle               | 7.29 us                                                                    | 7.25 us: 1.01x faster                                                     |
| tomli_loads          | 1.21 sec                                                                   | 1.22 sec: 1.00x slower                                                    |
| xml_etree_parse      | 91.5 ms                                                                    | 92.5 ms: 1.01x slower                                                     |
| json_loads           | 14.1 us                                                                    | 14.2 us: 1.01x slower                                                     |
| xml_etree_generate   | 51.2 ms                                                                    | 51.7 ms: 1.01x slower                                                     |
| unpickle_list        | 2.82 us                                                                    | 2.87 us: 1.02x slower                                                     |
| pickle_list          | 2.73 us                                                                    | 2.82 us: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                              |

Benchmark hidden because not significant (4): xml_etree_iterparse, xml_etree_process, pickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 21.8 ms                                                                    | 20.5 ms: 1.06x faster                                                     |
| python_startup_no_site | 17.8 ms                                                                    | 17.0 ms: 1.05x faster                                                     |
| Geometric mean         | (ref)                                                                      | 1.06x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 18.1 ms                                                                    | 18.0 ms: 1.01x faster                                                     |
| genshi_xml      | 44.6 ms                                                                    | 45.7 ms: 1.02x slower                                                     |
| django_template | 25.2 ms                                                                    | 26.1 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                                      | 1.01x slower                                                              |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|--------------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| richards                 | 30.1 ms                                                                    | 27.8 ms: 1.08x faster                                                     |
| richards_super           | 33.8 ms                                                                    | 31.4 ms: 1.08x faster                                                     |
| python_startup           | 21.8 ms                                                                    | 20.5 ms: 1.06x faster                                                     |
| mdp                      | 1.49 sec                                                                   | 1.40 sec: 1.06x faster                                                    |
| python_startup_no_site   | 17.8 ms                                                                    | 17.0 ms: 1.05x faster                                                     |
| coverage                 | 45.8 ms                                                                    | 44.1 ms: 1.04x faster                                                     |
| json_dumps               | 5.75 ms                                                                    | 5.62 ms: 1.02x faster                                                     |
| sqlglot_optimize         | 37.3 ms                                                                    | 36.6 ms: 1.02x faster                                                     |
| generators               | 21.6 ms                                                                    | 21.1 ms: 1.02x faster                                                     |
| raytrace                 | 178 ms                                                                     | 175 ms: 1.02x faster                                                      |
| hexiom                   | 4.67 ms                                                                    | 4.60 ms: 1.02x faster                                                     |
| go                       | 93.8 ms                                                                    | 92.4 ms: 1.02x faster                                                     |
| pickle_dict              | 17.8 us                                                                    | 17.6 us: 1.01x faster                                                     |
| crypto_pyaes             | 41.6 ms                                                                    | 41.0 ms: 1.01x faster                                                     |
| bench_mp_pool            | 69.3 ms                                                                    | 68.4 ms: 1.01x faster                                                     |
| deepcopy_memo            | 20.9 us                                                                    | 20.7 us: 1.01x faster                                                     |
| logging_silent           | 55.4 ns                                                                    | 54.8 ns: 1.01x faster                                                     |
| sqlglot_parse            | 808 us                                                                     | 799 us: 1.01x faster                                                      |
| sympy_sum                | 94.3 ms                                                                    | 93.3 ms: 1.01x faster                                                     |
| scimark_sor              | 84.7 ms                                                                    | 83.8 ms: 1.01x faster                                                     |
| regex_dna                | 118 ms                                                                     | 116 ms: 1.01x faster                                                      |
| scimark_fft              | 150 ms                                                                     | 148 ms: 1.01x faster                                                      |
| tornado_http             | 86.2 ms                                                                    | 85.5 ms: 1.01x faster                                                     |
| deepcopy                 | 239 us                                                                     | 237 us: 1.01x faster                                                      |
| meteor_contest           | 73.3 ms                                                                    | 72.7 ms: 1.01x faster                                                     |
| deltablue                | 2.35 ms                                                                    | 2.34 ms: 1.01x faster                                                     |
| unpickle_pure_python     | 129 us                                                                     | 128 us: 1.01x faster                                                      |
| genshi_text              | 18.1 ms                                                                    | 18.0 ms: 1.01x faster                                                     |
| pickle                   | 7.29 us                                                                    | 7.25 us: 1.01x faster                                                     |
| comprehensions           | 10.3 us                                                                    | 10.2 us: 1.01x faster                                                     |
| sqlglot_transpile        | 1.04 ms                                                                    | 1.03 ms: 1.00x faster                                                     |
| coroutines               | 13.1 ms                                                                    | 13.2 ms: 1.00x slower                                                     |
| tomli_loads              | 1.21 sec                                                                   | 1.22 sec: 1.00x slower                                                    |
| nqueens                  | 60.5 ms                                                                    | 60.8 ms: 1.00x slower                                                     |
| thrift                   | 508 us                                                                     | 511 us: 1.01x slower                                                      |
| pidigits                 | 149 ms                                                                     | 150 ms: 1.01x slower                                                      |
| pyflate                  | 257 ms                                                                     | 259 ms: 1.01x slower                                                      |
| bench_thread_pool        | 809 us                                                                     | 817 us: 1.01x slower                                                      |
| xml_etree_parse          | 91.5 ms                                                                    | 92.5 ms: 1.01x slower                                                     |
| json_loads               | 14.1 us                                                                    | 14.2 us: 1.01x slower                                                     |
| xml_etree_generate       | 51.2 ms                                                                    | 51.7 ms: 1.01x slower                                                     |
| async_generators         | 254 ms                                                                     | 257 ms: 1.01x slower                                                      |
| html5lib                 | 36.8 ms                                                                    | 37.2 ms: 1.01x slower                                                     |
| scimark_monte_carlo      | 37.7 ms                                                                    | 38.2 ms: 1.01x slower                                                     |
| logging_simple           | 5.84 us                                                                    | 5.92 us: 1.01x slower                                                     |
| logging_format           | 6.27 us                                                                    | 6.36 us: 1.01x slower                                                     |
| scimark_lu               | 69.1 ms                                                                    | 70.4 ms: 1.02x slower                                                     |
| unpickle_list            | 2.82 us                                                                    | 2.87 us: 1.02x slower                                                     |
| pprint_safe_repr         | 457 ms                                                                     | 467 ms: 1.02x slower                                                      |
| fannkuch                 | 217 ms                                                                     | 223 ms: 1.02x slower                                                      |
| typing_runtime_protocols | 112 us                                                                     | 115 us: 1.02x slower                                                      |
| genshi_xml               | 44.6 ms                                                                    | 45.7 ms: 1.02x slower                                                     |
| spectral_norm            | 44.2 ms                                                                    | 45.4 ms: 1.03x slower                                                     |
| telco                    | 4.55 ms                                                                    | 4.68 ms: 1.03x slower                                                     |
| pickle_list              | 2.73 us                                                                    | 2.82 us: 1.03x slower                                                     |
| django_template          | 25.2 ms                                                                    | 26.1 ms: 1.03x slower                                                     |
| json                     | 2.90 ms                                                                    | 3.03 ms: 1.04x slower                                                     |
| pycparser                | 716 ms                                                                     | 754 ms: 1.05x slower                                                      |
| nbody                    | 53.1 ms                                                                    | 56.2 ms: 1.06x slower                                                     |
| Geometric mean           | (ref)                                                                      | 1.00x faster                                                              |

Benchmark hidden because not significant (33): chaos, regex_v8, async_tree_cpu_io_mixed_tg, float, regex_effbot, sympy_integrate, sympy_str, docutils, xml_etree_iterparse, xml_etree_process, create_gc_cycles, regex_compile, pickle_pure_python, sympy_expand, scimark_sparse_mat_mult, sqlite_synth, asyncio_tcp, asyncio_tcp_ssl, 2to3, async_tree_io_tg, mako, unpickle, deepcopy_reduce, pathlib, gc_traversal, pprint_pformat, async_tree_cpu_io_mixed, pylint, async_tree_memoization, async_tree_io, async_tree_none, async_tree_none_tg, async_tree_memoization_tg

# HPT report

- Reliability score: 90.33% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown