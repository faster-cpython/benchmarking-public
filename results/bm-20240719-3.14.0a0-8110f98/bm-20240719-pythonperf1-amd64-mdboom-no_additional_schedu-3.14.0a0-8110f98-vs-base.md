# Results vs. base

- fork: mdboom
- ref: no_additional_schedu
- machine: windows-amd64
- commit hash: 8110f98
- commit date: 2024-07-19
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 227 ms                                                                     | 222 ms: 1.02x faster                                                       |
| docutils       | 1.67 sec                                                                   | 1.66 sec: 1.01x faster                                                     |
| html5lib       | 38.8 ms                                                                    | 38.3 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators | 245 ms                                                                     | 244 ms: 1.01x faster                                                       |
| Geometric mean   | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (11): asyncio_tcp, async_tree_io, asyncio_tcp_ssl, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization, coroutines, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 80.3 ms                                                                    | 75.5 ms: 1.06x faster                                                      |
| float          | 56.9 ms                                                                    | 56.0 ms: 1.02x faster                                                      |
| pidigits       | 151 ms                                                                     | 150 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                                      | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 17.4 ms                                                                    | 15.4 ms: 1.13x faster                                                      |
| regex_compile  | 85.8 ms                                                                    | 83.3 ms: 1.03x faster                                                      |
| regex_dna      | 124 ms                                                                     | 127 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                      | 1.03x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 209 us                                                                     | 199 us: 1.05x faster                                                       |
| unpickle_pure_python | 150 us                                                                     | 145 us: 1.03x faster                                                       |
| xml_etree_process    | 41.1 ms                                                                    | 39.9 ms: 1.03x faster                                                      |
| xml_etree_generate   | 59.1 ms                                                                    | 57.5 ms: 1.03x faster                                                      |
| json_dumps           | 6.09 ms                                                                    | 5.95 ms: 1.02x faster                                                      |
| json_loads           | 14.4 us                                                                    | 14.5 us: 1.01x slower                                                      |
| tomli_loads          | 1.57 sec                                                                   | 1.58 sec: 1.01x slower                                                     |
| xml_etree_parse      | 92.5 ms                                                                    | 93.8 ms: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 21.2 ms                                                                    | 21.5 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text    | 16.8 ms                                                                    | 16.0 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (3): django_template, mako, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|--------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8                 | 17.4 ms                                                                    | 15.4 ms: 1.13x faster                                                      |
| pycparser                | 848 ms                                                                     | 755 ms: 1.12x faster                                                       |
| scimark_sor              | 84.4 ms                                                                    | 78.9 ms: 1.07x faster                                                      |
| nbody                    | 80.3 ms                                                                    | 75.5 ms: 1.06x faster                                                      |
| scimark_lu               | 65.6 ms                                                                    | 62.2 ms: 1.05x faster                                                      |
| genshi_text              | 16.8 ms                                                                    | 16.0 ms: 1.05x faster                                                      |
| pickle_pure_python       | 209 us                                                                     | 199 us: 1.05x faster                                                       |
| go                       | 93.5 ms                                                                    | 89.2 ms: 1.05x faster                                                      |
| scimark_fft              | 213 ms                                                                     | 204 ms: 1.05x faster                                                       |
| deltablue                | 2.17 ms                                                                    | 2.08 ms: 1.04x faster                                                      |
| richards_super           | 33.4 ms                                                                    | 32.0 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult  | 2.98 ms                                                                    | 2.86 ms: 1.04x faster                                                      |
| pyflate                  | 315 ms                                                                     | 302 ms: 1.04x faster                                                       |
| hexiom                   | 4.30 ms                                                                    | 4.13 ms: 1.04x faster                                                      |
| chaos                    | 43.6 ms                                                                    | 41.9 ms: 1.04x faster                                                      |
| crypto_pyaes             | 51.5 ms                                                                    | 49.5 ms: 1.04x faster                                                      |
| telco                    | 4.97 ms                                                                    | 4.79 ms: 1.04x faster                                                      |
| scimark_monte_carlo      | 48.4 ms                                                                    | 46.6 ms: 1.04x faster                                                      |
| coverage                 | 48.2 ms                                                                    | 46.4 ms: 1.04x faster                                                      |
| richards                 | 29.6 ms                                                                    | 28.5 ms: 1.04x faster                                                      |
| sqlglot_parse            | 891 us                                                                     | 861 us: 1.03x faster                                                       |
| unpickle_pure_python     | 150 us                                                                     | 145 us: 1.03x faster                                                       |
| generators               | 22.3 ms                                                                    | 21.7 ms: 1.03x faster                                                      |
| deepcopy_memo            | 21.0 us                                                                    | 20.3 us: 1.03x faster                                                      |
| regex_compile            | 85.8 ms                                                                    | 83.3 ms: 1.03x faster                                                      |
| fannkuch                 | 291 ms                                                                     | 282 ms: 1.03x faster                                                       |
| xml_etree_process        | 41.1 ms                                                                    | 39.9 ms: 1.03x faster                                                      |
| xml_etree_generate       | 59.1 ms                                                                    | 57.5 ms: 1.03x faster                                                      |
| sqlglot_transpile        | 1.11 ms                                                                    | 1.08 ms: 1.03x faster                                                      |
| raytrace                 | 177 ms                                                                     | 173 ms: 1.03x faster                                                       |
| deepcopy                 | 182 us                                                                     | 178 us: 1.02x faster                                                       |
| create_gc_cycles         | 911 us                                                                     | 890 us: 1.02x faster                                                       |
| json_dumps               | 6.09 ms                                                                    | 5.95 ms: 1.02x faster                                                      |
| comprehensions           | 11.8 us                                                                    | 11.5 us: 1.02x faster                                                      |
| spectral_norm            | 68.2 ms                                                                    | 66.7 ms: 1.02x faster                                                      |
| 2to3                     | 227 ms                                                                     | 222 ms: 1.02x faster                                                       |
| mdp                      | 1.43 sec                                                                   | 1.40 sec: 1.02x faster                                                     |
| sympy_integrate          | 13.0 ms                                                                    | 12.8 ms: 1.02x faster                                                      |
| sympy_sum                | 88.7 ms                                                                    | 86.9 ms: 1.02x faster                                                      |
| thrift                   | 540 us                                                                     | 529 us: 1.02x faster                                                       |
| sqlglot_normalize        | 188 ms                                                                     | 185 ms: 1.02x faster                                                       |
| logging_silent           | 61.8 ns                                                                    | 60.6 ns: 1.02x faster                                                      |
| pprint_pformat           | 1.11 sec                                                                   | 1.09 sec: 1.02x faster                                                     |
| sqlglot_optimize         | 35.2 ms                                                                    | 34.6 ms: 1.02x faster                                                      |
| deepcopy_reduce          | 1.86 us                                                                    | 1.82 us: 1.02x faster                                                      |
| logging_simple           | 6.31 us                                                                    | 6.20 us: 1.02x faster                                                      |
| sympy_expand             | 293 ms                                                                     | 288 ms: 1.02x faster                                                       |
| sympy_str                | 171 ms                                                                     | 169 ms: 1.02x faster                                                       |
| pprint_safe_repr         | 543 ms                                                                     | 534 ms: 1.02x faster                                                       |
| float                    | 56.9 ms                                                                    | 56.0 ms: 1.02x faster                                                      |
| logging_format           | 6.75 us                                                                    | 6.66 us: 1.01x faster                                                      |
| html5lib                 | 38.8 ms                                                                    | 38.3 ms: 1.01x faster                                                      |
| nqueens                  | 61.8 ms                                                                    | 61.2 ms: 1.01x faster                                                      |
| gc_traversal             | 1.57 ms                                                                    | 1.56 ms: 1.01x faster                                                      |
| docutils                 | 1.67 sec                                                                   | 1.66 sec: 1.01x faster                                                     |
| pathlib                  | 81.2 ms                                                                    | 80.6 ms: 1.01x faster                                                      |
| async_generators         | 245 ms                                                                     | 244 ms: 1.01x faster                                                       |
| bench_mp_pool            | 67.8 ms                                                                    | 67.4 ms: 1.01x faster                                                      |
| pidigits                 | 151 ms                                                                     | 150 ms: 1.00x faster                                                       |
| meteor_contest           | 77.0 ms                                                                    | 76.8 ms: 1.00x faster                                                      |
| json_loads               | 14.4 us                                                                    | 14.5 us: 1.01x slower                                                      |
| tomli_loads              | 1.57 sec                                                                   | 1.58 sec: 1.01x slower                                                     |
| xml_etree_parse          | 92.5 ms                                                                    | 93.8 ms: 1.01x slower                                                      |
| python_startup           | 21.2 ms                                                                    | 21.5 ms: 1.02x slower                                                      |
| typing_runtime_protocols | 109 us                                                                     | 111 us: 1.02x slower                                                       |
| regex_dna                | 124 ms                                                                     | 127 ms: 1.02x slower                                                       |
| Geometric mean           | (ref)                                                                      | 1.02x faster                                                               |

Benchmark hidden because not significant (21): asyncio_tcp, bench_thread_pool, async_tree_io, asyncio_tcp_ssl, pylint, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed, django_template, json, async_tree_memoization, coroutines, async_tree_cpu_io_mixed_tg, regex_effbot, mako, tornado_http, xml_etree_iterparse, async_tree_memoization_tg, async_tree_io_tg, python_startup_no_site, genshi_xml

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown