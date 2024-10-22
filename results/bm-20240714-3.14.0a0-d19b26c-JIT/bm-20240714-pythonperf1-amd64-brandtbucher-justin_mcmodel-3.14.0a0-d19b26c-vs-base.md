# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel
- machine: windows-amd64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 232 ms                                                                     | 234 ms: 1.01x slower                                                       |
| docutils       | 1.75 sec                                                                   | 1.78 sec: 1.02x slower                                                     |
| html5lib       | 38.9 ms                                                                    | 41.9 ms: 1.08x slower                                                      |
| tornado_http   | 83.8 ms                                                                    | 85.4 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, async_tree_memoization, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 53.4 ms                                                                    | 51.1 ms: 1.05x faster                                                      |
| pidigits       | 149 ms                                                                     | 149 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 122 ms                                                                     | 120 ms: 1.01x faster                                                       |
| regex_compile  | 89.1 ms                                                                    | 90.2 ms: 1.01x slower                                                      |
| regex_v8       | 16.1 ms                                                                    | 23.9 ms: 1.48x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.10x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.5 ms                                                                    | 93.4 ms: 1.01x slower                                                      |
| xml_etree_generate   | 52.2 ms                                                                    | 52.8 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 60.7 ms                                                                    | 62.1 ms: 1.02x slower                                                      |
| unpickle_pure_python | 130 us                                                                     | 134 us: 1.03x slower                                                       |
| pickle_pure_python   | 174 us                                                                     | 179 us: 1.03x slower                                                       |
| xml_etree_process    | 36.7 ms                                                                    | 38.1 ms: 1.04x slower                                                      |
| tomli_loads          | 1.23 sec                                                                   | 1.28 sec: 1.04x slower                                                     |
| Geometric mean       | (ref)                                                                      | 1.02x slower                                                               |

Benchmark hidden because not significant (2): json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.5 ms                                                                    | 17.1 ms: 1.03x faster                                                      |
| python_startup         | 21.0 ms                                                                    | 20.9 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                                      | 1.02x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 46.9 ms                                                                    | 44.8 ms: 1.05x faster                                                      |
| django_template | 26.1 ms                                                                    | 26.3 ms: 1.01x slower                                                      |
| genshi_text     | 17.9 ms                                                                    | 18.2 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|--------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml               | 46.9 ms                                                                    | 44.8 ms: 1.05x faster                                                      |
| nbody                    | 53.4 ms                                                                    | 51.1 ms: 1.05x faster                                                      |
| python_startup_no_site   | 17.5 ms                                                                    | 17.1 ms: 1.03x faster                                                      |
| typing_runtime_protocols | 115 us                                                                     | 112 us: 1.02x faster                                                       |
| regex_dna                | 122 ms                                                                     | 120 ms: 1.01x faster                                                       |
| python_startup           | 21.0 ms                                                                    | 20.9 ms: 1.01x faster                                                      |
| pathlib                  | 75.5 ms                                                                    | 74.9 ms: 1.01x faster                                                      |
| scimark_sparse_mat_mult  | 2.18 ms                                                                    | 2.17 ms: 1.01x faster                                                      |
| pprint_safe_repr         | 464 ms                                                                     | 462 ms: 1.00x faster                                                       |
| pidigits                 | 149 ms                                                                     | 149 ms: 1.00x slower                                                       |
| sqlglot_transpile        | 1.03 ms                                                                    | 1.04 ms: 1.01x slower                                                      |
| xml_etree_parse          | 92.5 ms                                                                    | 93.4 ms: 1.01x slower                                                      |
| deepcopy_memo            | 15.5 us                                                                    | 15.6 us: 1.01x slower                                                      |
| 2to3                     | 232 ms                                                                     | 234 ms: 1.01x slower                                                       |
| django_template          | 26.1 ms                                                                    | 26.3 ms: 1.01x slower                                                      |
| fannkuch                 | 222 ms                                                                     | 225 ms: 1.01x slower                                                       |
| regex_compile            | 89.1 ms                                                                    | 90.2 ms: 1.01x slower                                                      |
| meteor_contest           | 73.2 ms                                                                    | 74.1 ms: 1.01x slower                                                      |
| xml_etree_generate       | 52.2 ms                                                                    | 52.8 ms: 1.01x slower                                                      |
| logging_silent           | 56.5 ns                                                                    | 57.3 ns: 1.01x slower                                                      |
| bench_thread_pool        | 797 us                                                                     | 808 us: 1.01x slower                                                       |
| scimark_monte_carlo      | 37.6 ms                                                                    | 38.1 ms: 1.01x slower                                                      |
| genshi_text              | 17.9 ms                                                                    | 18.2 ms: 1.01x slower                                                      |
| sympy_integrate          | 13.8 ms                                                                    | 14.0 ms: 1.01x slower                                                      |
| crypto_pyaes             | 40.2 ms                                                                    | 40.8 ms: 1.01x slower                                                      |
| sympy_sum                | 92.6 ms                                                                    | 94.0 ms: 1.02x slower                                                      |
| pyflate                  | 256 ms                                                                     | 260 ms: 1.02x slower                                                       |
| docutils                 | 1.75 sec                                                                   | 1.78 sec: 1.02x slower                                                     |
| deepcopy                 | 177 us                                                                     | 180 us: 1.02x slower                                                       |
| tornado_http             | 83.8 ms                                                                    | 85.4 ms: 1.02x slower                                                      |
| sqlglot_parse            | 800 us                                                                     | 815 us: 1.02x slower                                                       |
| xml_etree_iterparse      | 60.7 ms                                                                    | 62.1 ms: 1.02x slower                                                      |
| deepcopy_reduce          | 1.76 us                                                                    | 1.80 us: 1.02x slower                                                      |
| nqueens                  | 60.5 ms                                                                    | 61.9 ms: 1.02x slower                                                      |
| async_generators         | 253 ms                                                                     | 259 ms: 1.02x slower                                                       |
| sqlglot_normalize        | 188 ms                                                                     | 193 ms: 1.03x slower                                                       |
| sqlglot_optimize         | 35.5 ms                                                                    | 36.4 ms: 1.03x slower                                                      |
| richards                 | 29.8 ms                                                                    | 30.6 ms: 1.03x slower                                                      |
| sympy_str                | 179 ms                                                                     | 184 ms: 1.03x slower                                                       |
| sympy_expand             | 310 ms                                                                     | 319 ms: 1.03x slower                                                       |
| thrift                   | 513 us                                                                     | 528 us: 1.03x slower                                                       |
| coroutines               | 13.9 ms                                                                    | 14.3 ms: 1.03x slower                                                      |
| logging_simple           | 5.63 us                                                                    | 5.80 us: 1.03x slower                                                      |
| spectral_norm            | 44.5 ms                                                                    | 45.8 ms: 1.03x slower                                                      |
| chaos                    | 38.8 ms                                                                    | 40.0 ms: 1.03x slower                                                      |
| unpickle_pure_python     | 130 us                                                                     | 134 us: 1.03x slower                                                       |
| pickle_pure_python       | 174 us                                                                     | 179 us: 1.03x slower                                                       |
| scimark_lu               | 74.6 ms                                                                    | 77.0 ms: 1.03x slower                                                      |
| logging_format           | 6.08 us                                                                    | 6.27 us: 1.03x slower                                                      |
| richards_super           | 33.6 ms                                                                    | 34.8 ms: 1.04x slower                                                      |
| xml_etree_process        | 36.7 ms                                                                    | 38.1 ms: 1.04x slower                                                      |
| deltablue                | 2.26 ms                                                                    | 2.35 ms: 1.04x slower                                                      |
| mdp                      | 1.41 sec                                                                   | 1.46 sec: 1.04x slower                                                     |
| tomli_loads              | 1.23 sec                                                                   | 1.28 sec: 1.04x slower                                                     |
| coverage                 | 46.5 ms                                                                    | 48.5 ms: 1.04x slower                                                      |
| raytrace                 | 176 ms                                                                     | 185 ms: 1.05x slower                                                       |
| go                       | 93.0 ms                                                                    | 97.7 ms: 1.05x slower                                                      |
| scimark_sor              | 86.5 ms                                                                    | 91.6 ms: 1.06x slower                                                      |
| generators               | 23.5 ms                                                                    | 25.0 ms: 1.07x slower                                                      |
| html5lib                 | 38.9 ms                                                                    | 41.9 ms: 1.08x slower                                                      |
| telco                    | 4.49 ms                                                                    | 4.95 ms: 1.10x slower                                                      |
| regex_v8                 | 16.1 ms                                                                    | 23.9 ms: 1.48x slower                                                      |
| Geometric mean           | (ref)                                                                      | 1.02x slower                                                               |

Benchmark hidden because not significant (25): pycparser, comprehensions, pprint_pformat, json_dumps, hexiom, gc_traversal, bench_mp_pool, regex_effbot, create_gc_cycles, async_tree_cpu_io_mixed, mako, scimark_fft, json_loads, float, async_tree_cpu_io_mixed_tg, json, asyncio_tcp_ssl, async_tree_memoization_tg, pylint, async_tree_io_tg, async_tree_none, async_tree_memoization, asyncio_tcp, async_tree_none_tg, async_tree_io

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown