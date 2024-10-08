# Results vs. base

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-amd64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.01x faster
- HPT reliability: 96.65%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| docutils       | 1.77 sec                                                                   | 1.75 sec: 1.01x faster                                                               |
| html5lib       | 42.1 ms                                                                    | 42.3 ms: 1.00x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_generators | 248 ms                                                                     | 244 ms: 1.02x faster                                                                 |
| coroutines       | 14.0 ms                                                                    | 14.3 ms: 1.02x slower                                                                |
| asyncio_tcp_ssl  | 1.53 sec                                                                   | 1.85 sec: 1.21x slower                                                               |
| Geometric mean   | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_io, async_tree_io_tg, async_tree_none, async_tree_memoization_tg, asyncio_tcp, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                                     | 151 ms: 1.01x slower                                                                 |
| nbody          | 85.8 ms                                                                    | 92.0 ms: 1.07x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.03x slower                                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 17.4 ms                                                                    | 14.8 ms: 1.17x faster                                                                |
| regex_dna      | 121 ms                                                                     | 120 ms: 1.01x faster                                                                 |
| regex_compile  | 93.3 ms                                                                    | 95.0 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.04x faster                                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_process    | 42.2 ms                                                                    | 41.1 ms: 1.03x faster                                                                |
| tomli_loads          | 1.63 sec                                                                   | 1.61 sec: 1.01x faster                                                               |
| xml_etree_generate   | 58.8 ms                                                                    | 58.1 ms: 1.01x faster                                                                |
| xml_etree_parse      | 93.1 ms                                                                    | 94.8 ms: 1.02x slower                                                                |
| unpickle_pure_python | 152 us                                                                     | 157 us: 1.03x slower                                                                 |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (4): pickle_pure_python, json_loads, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 17.7 ms                                                                    | 17.4 ms: 1.02x faster                                                                |
| python_startup         | 22.0 ms                                                                    | 21.7 ms: 1.02x faster                                                                |
| Geometric mean         | (ref)                                                                      | 1.02x faster                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_xml      | 39.5 ms                                                                    | 36.8 ms: 1.07x faster                                                                |
| django_template | 25.6 ms                                                                    | 24.7 ms: 1.04x faster                                                                |
| mako            | 7.40 ms                                                                    | 7.25 ms: 1.02x faster                                                                |
| genshi_text     | 18.0 ms                                                                    | 17.9 ms: 1.00x faster                                                                |
| Geometric mean  | (ref)                                                                      | 1.03x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pycparser                | 912 ms                                                                     | 752 ms: 1.21x faster                                                                 |
| regex_v8                 | 17.4 ms                                                                    | 14.8 ms: 1.17x faster                                                                |
| genshi_xml               | 39.5 ms                                                                    | 36.8 ms: 1.07x faster                                                                |
| coverage                 | 49.4 ms                                                                    | 47.4 ms: 1.04x faster                                                                |
| deepcopy_reduce          | 2.03 us                                                                    | 1.95 us: 1.04x faster                                                                |
| django_template          | 25.6 ms                                                                    | 24.7 ms: 1.04x faster                                                                |
| typing_runtime_protocols | 116 us                                                                     | 112 us: 1.04x faster                                                                 |
| raytrace                 | 202 ms                                                                     | 196 ms: 1.03x faster                                                                 |
| thrift                   | 541 us                                                                     | 525 us: 1.03x faster                                                                 |
| comprehensions           | 12.4 us                                                                    | 12.1 us: 1.03x faster                                                                |
| scimark_monte_carlo      | 52.6 ms                                                                    | 51.2 ms: 1.03x faster                                                                |
| xml_etree_process        | 42.2 ms                                                                    | 41.1 ms: 1.03x faster                                                                |
| telco                    | 5.06 ms                                                                    | 4.93 ms: 1.03x faster                                                                |
| mako                     | 7.40 ms                                                                    | 7.25 ms: 1.02x faster                                                                |
| deepcopy                 | 196 us                                                                     | 192 us: 1.02x faster                                                                 |
| create_gc_cycles         | 902 us                                                                     | 885 us: 1.02x faster                                                                 |
| sqlglot_normalize        | 197 ms                                                                     | 193 ms: 1.02x faster                                                                 |
| python_startup_no_site   | 17.7 ms                                                                    | 17.4 ms: 1.02x faster                                                                |
| async_generators         | 248 ms                                                                     | 244 ms: 1.02x faster                                                                 |
| python_startup           | 22.0 ms                                                                    | 21.7 ms: 1.02x faster                                                                |
| sqlglot_optimize         | 36.8 ms                                                                    | 36.3 ms: 1.01x faster                                                                |
| scimark_lu               | 66.4 ms                                                                    | 65.5 ms: 1.01x faster                                                                |
| tomli_loads              | 1.63 sec                                                                   | 1.61 sec: 1.01x faster                                                               |
| richards_super           | 37.5 ms                                                                    | 37.0 ms: 1.01x faster                                                                |
| xml_etree_generate       | 58.8 ms                                                                    | 58.1 ms: 1.01x faster                                                                |
| pprint_safe_repr         | 574 ms                                                                     | 569 ms: 1.01x faster                                                                 |
| regex_dna                | 121 ms                                                                     | 120 ms: 1.01x faster                                                                 |
| deepcopy_memo            | 21.3 us                                                                    | 21.1 us: 1.01x faster                                                                |
| pprint_pformat           | 1.17 sec                                                                   | 1.16 sec: 1.01x faster                                                               |
| richards                 | 33.1 ms                                                                    | 32.8 ms: 1.01x faster                                                                |
| docutils                 | 1.77 sec                                                                   | 1.75 sec: 1.01x faster                                                               |
| sqlglot_parse            | 913 us                                                                     | 906 us: 1.01x faster                                                                 |
| gc_traversal             | 1.56 ms                                                                    | 1.55 ms: 1.01x faster                                                                |
| dulwich_log              | 42.9 ms                                                                    | 42.7 ms: 1.01x faster                                                                |
| logging_format           | 6.92 us                                                                    | 6.89 us: 1.01x faster                                                                |
| genshi_text              | 18.0 ms                                                                    | 17.9 ms: 1.00x faster                                                                |
| mdp                      | 1.47 sec                                                                   | 1.46 sec: 1.00x faster                                                               |
| sympy_expand             | 310 ms                                                                     | 311 ms: 1.00x slower                                                                 |
| html5lib                 | 42.1 ms                                                                    | 42.3 ms: 1.00x slower                                                                |
| pidigits                 | 150 ms                                                                     | 151 ms: 1.01x slower                                                                 |
| sympy_integrate          | 13.4 ms                                                                    | 13.5 ms: 1.01x slower                                                                |
| fannkuch                 | 298 ms                                                                     | 301 ms: 1.01x slower                                                                 |
| scimark_sparse_mat_mult  | 2.85 ms                                                                    | 2.88 ms: 1.01x slower                                                                |
| pyflate                  | 325 ms                                                                     | 330 ms: 1.01x slower                                                                 |
| meteor_contest           | 77.9 ms                                                                    | 79.0 ms: 1.01x slower                                                                |
| xml_etree_parse          | 93.1 ms                                                                    | 94.8 ms: 1.02x slower                                                                |
| regex_compile            | 93.3 ms                                                                    | 95.0 ms: 1.02x slower                                                                |
| coroutines               | 14.0 ms                                                                    | 14.3 ms: 1.02x slower                                                                |
| nqueens                  | 63.4 ms                                                                    | 64.9 ms: 1.02x slower                                                                |
| unpickle_pure_python     | 152 us                                                                     | 157 us: 1.03x slower                                                                 |
| spectral_norm            | 71.8 ms                                                                    | 74.1 ms: 1.03x slower                                                                |
| generators               | 21.2 ms                                                                    | 22.0 ms: 1.04x slower                                                                |
| json                     | 3.03 ms                                                                    | 3.17 ms: 1.05x slower                                                                |
| scimark_sor              | 92.2 ms                                                                    | 96.5 ms: 1.05x slower                                                                |
| nbody                    | 85.8 ms                                                                    | 92.0 ms: 1.07x slower                                                                |
| asyncio_tcp_ssl          | 1.53 sec                                                                   | 1.85 sec: 1.21x slower                                                               |
| Geometric mean           | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (32): async_tree_none_tg, async_tree_io, async_tree_io_tg, async_tree_none, async_tree_memoization_tg, asyncio_tcp, async_tree_cpu_io_mixed_tg, bench_mp_pool, regex_effbot, deltablue, crypto_pyaes, async_tree_cpu_io_mixed, tornado_http, sympy_str, pathlib, chaos, go, pylint, scimark_fft, hexiom, logging_silent, sympy_sum, sqlglot_transpile, pickle_pure_python, logging_simple, async_tree_memoization, json_loads, float, 2to3, bench_thread_pool, xml_etree_iterparse, json_dumps

# HPT report

- Reliability score: 96.65% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown