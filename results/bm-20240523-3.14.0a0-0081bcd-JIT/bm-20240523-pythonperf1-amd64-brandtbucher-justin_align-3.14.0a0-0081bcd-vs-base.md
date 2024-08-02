# Results vs. base

- fork: brandtbucher
- ref: justin_align
- machine: windows-amd64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.00x faster
- HPT reliability: 94.77%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 235 ms                                                                     | 233 ms: 1.01x faster                                                     |
| chameleon      | 5.13 ms                                                                    | 5.08 ms: 1.01x faster                                                    |
| docutils       | 1.79 sec                                                                   | 1.77 sec: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                             |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg, async_tree_none, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 45.2 ms                                                                    | 44.6 ms: 1.01x faster                                                    |
| pidigits       | 149 ms                                                                     | 149 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 16.2 ms                                                                    | 14.8 ms: 1.09x faster                                                    |
| regex_compile  | 89.3 ms                                                                    | 87.4 ms: 1.02x faster                                                    |
| regex_effbot   | 1.60 ms                                                                    | 1.58 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                      | 1.03x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                                    | 13.9 us: 1.02x faster                                                    |
| unpickle_pure_python | 129 us                                                                     | 127 us: 1.02x faster                                                     |
| pickle_dict          | 18.0 us                                                                    | 17.8 us: 1.01x faster                                                    |
| xml_etree_parse      | 89.4 ms                                                                    | 89.9 ms: 1.01x slower                                                    |
| unpickle             | 8.57 us                                                                    | 8.68 us: 1.01x slower                                                    |
| pickle               | 7.35 us                                                                    | 7.55 us: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                             |

Benchmark hidden because not significant (8): xml_etree_process, xml_etree_generate, json_dumps, xml_etree_iterparse, unpickle_list, pickle_pure_python, tomli_loads, pickle_list

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 26.1 ms                                                                    | 25.6 ms: 1.02x faster                                                    |
| genshi_text     | 18.3 ms                                                                    | 18.9 ms: 1.04x slower                                                    |
| Geometric mean  | (ref)                                                                      | 1.01x slower                                                             |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|--------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8                 | 16.2 ms                                                                    | 14.8 ms: 1.09x faster                                                    |
| scimark_lu               | 73.1 ms                                                                    | 67.8 ms: 1.08x faster                                                    |
| nqueens                  | 62.7 ms                                                                    | 60.1 ms: 1.04x faster                                                    |
| deepcopy_memo            | 20.9 us                                                                    | 20.3 us: 1.03x faster                                                    |
| generators               | 21.8 ms                                                                    | 21.3 ms: 1.03x faster                                                    |
| logging_silent           | 56.8 ns                                                                    | 55.5 ns: 1.02x faster                                                    |
| pprint_pformat           | 941 ms                                                                     | 920 ms: 1.02x faster                                                     |
| django_template          | 26.1 ms                                                                    | 25.6 ms: 1.02x faster                                                    |
| regex_compile            | 89.3 ms                                                                    | 87.4 ms: 1.02x faster                                                    |
| richards_super           | 34.1 ms                                                                    | 33.4 ms: 1.02x faster                                                    |
| sqlglot_transpile        | 1.05 ms                                                                    | 1.03 ms: 1.02x faster                                                    |
| json_loads               | 14.2 us                                                                    | 13.9 us: 1.02x faster                                                    |
| thrift                   | 516 us                                                                     | 506 us: 1.02x faster                                                     |
| sqlglot_optimize         | 37.3 ms                                                                    | 36.7 ms: 1.02x faster                                                    |
| sympy_sum                | 94.9 ms                                                                    | 93.3 ms: 1.02x faster                                                    |
| unpickle_pure_python     | 129 us                                                                     | 127 us: 1.02x faster                                                     |
| pprint_safe_repr         | 460 ms                                                                     | 453 ms: 1.01x faster                                                     |
| richards                 | 29.9 ms                                                                    | 29.5 ms: 1.01x faster                                                    |
| float                    | 45.2 ms                                                                    | 44.6 ms: 1.01x faster                                                    |
| json                     | 2.91 ms                                                                    | 2.88 ms: 1.01x faster                                                    |
| sqlglot_parse            | 813 us                                                                     | 803 us: 1.01x faster                                                     |
| pathlib                  | 79.5 ms                                                                    | 78.7 ms: 1.01x faster                                                    |
| sympy_integrate          | 14.1 ms                                                                    | 13.9 ms: 1.01x faster                                                    |
| sympy_expand             | 315 ms                                                                     | 312 ms: 1.01x faster                                                     |
| typing_runtime_protocols | 114 us                                                                     | 113 us: 1.01x faster                                                     |
| hexiom                   | 4.71 ms                                                                    | 4.66 ms: 1.01x faster                                                    |
| chameleon                | 5.13 ms                                                                    | 5.08 ms: 1.01x faster                                                    |
| regex_effbot             | 1.60 ms                                                                    | 1.58 ms: 1.01x faster                                                    |
| docutils                 | 1.79 sec                                                                   | 1.77 sec: 1.01x faster                                                   |
| 2to3                     | 235 ms                                                                     | 233 ms: 1.01x faster                                                     |
| deltablue                | 2.38 ms                                                                    | 2.37 ms: 1.01x faster                                                    |
| pickle_dict              | 18.0 us                                                                    | 17.8 us: 1.01x faster                                                    |
| sympy_str                | 179 ms                                                                     | 178 ms: 1.01x faster                                                     |
| raytrace                 | 177 ms                                                                     | 176 ms: 1.00x faster                                                     |
| scimark_monte_carlo      | 38.1 ms                                                                    | 37.9 ms: 1.00x faster                                                    |
| pidigits                 | 149 ms                                                                     | 149 ms: 1.00x slower                                                     |
| scimark_sparse_mat_mult  | 2.13 ms                                                                    | 2.14 ms: 1.00x slower                                                    |
| xml_etree_parse          | 89.4 ms                                                                    | 89.9 ms: 1.01x slower                                                    |
| go                       | 93.6 ms                                                                    | 94.5 ms: 1.01x slower                                                    |
| async_generators         | 252 ms                                                                     | 254 ms: 1.01x slower                                                     |
| scimark_sor              | 82.4 ms                                                                    | 83.4 ms: 1.01x slower                                                    |
| unpickle                 | 8.57 us                                                                    | 8.68 us: 1.01x slower                                                    |
| deepcopy_reduce          | 2.06 us                                                                    | 2.09 us: 1.02x slower                                                    |
| create_gc_cycles         | 890 us                                                                     | 904 us: 1.02x slower                                                     |
| scimark_fft              | 147 ms                                                                     | 149 ms: 1.02x slower                                                     |
| deepcopy                 | 237 us                                                                     | 242 us: 1.02x slower                                                     |
| pickle                   | 7.35 us                                                                    | 7.55 us: 1.03x slower                                                    |
| sqlite_synth             | 1.57 us                                                                    | 1.62 us: 1.03x slower                                                    |
| coverage                 | 44.4 ms                                                                    | 46.0 ms: 1.03x slower                                                    |
| genshi_text              | 18.3 ms                                                                    | 18.9 ms: 1.04x slower                                                    |
| spectral_norm            | 45.4 ms                                                                    | 47.8 ms: 1.05x slower                                                    |
| fannkuch                 | 218 ms                                                                     | 230 ms: 1.05x slower                                                     |
| mdp                      | 1.40 sec                                                                   | 1.49 sec: 1.06x slower                                                   |
| pycparser                | 742 ms                                                                     | 803 ms: 1.08x slower                                                     |
| Geometric mean           | (ref)                                                                      | 1.00x faster                                                             |

Benchmark hidden because not significant (40): bench_thread_pool, tornado_http, regex_dna, mako, pylint, python_startup, xml_etree_process, bench_mp_pool, async_tree_cpu_io_mixed_tg, crypto_pyaes, xml_etree_generate, logging_simple, json_dumps, nbody, pyflate, html5lib, xml_etree_iterparse, flaskblogging, unpickle_list, gc_traversal, meteor_contest, logging_format, chaos, async_tree_cpu_io_mixed, asyncio_tcp, telco, async_tree_io, pickle_pure_python, async_tree_io_tg, async_tree_none, python_startup_no_site, tomli_loads, comprehensions, asyncio_tcp_ssl, coroutines, async_tree_memoization, genshi_xml, async_tree_memoization_tg, pickle_list, async_tree_none_tg

# HPT report

- Reliability score: 94.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown