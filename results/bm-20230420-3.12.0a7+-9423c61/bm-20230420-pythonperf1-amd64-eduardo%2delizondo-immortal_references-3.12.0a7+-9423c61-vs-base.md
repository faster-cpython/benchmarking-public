
# Results vs. base

- fork: eduardo-elizondo
- ref: immortal_references
- machine: windows-amd64
- commit hash: 9423c61
- commit date: 2023-04-20
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230415-pythonperf1-amd64-python-main-3.12.0a7+-4fe1c4b | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 198 ms                                                      | 204 ms: 1.03x slower                                                                   |
| chameleon      | 4.67 ms                                                     | 4.88 ms: 1.04x slower                                                                  |
| docutils       | 1.49 sec                                                    | 1.56 sec: 1.05x slower                                                                 |
| html5lib       | 35.4 ms                                                     | 36.4 ms: 1.03x slower                                                                  |
| tornado_http   | 85.4 ms                                                     | 88.8 ms: 1.04x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230415-pythonperf1-amd64-python-main-3.12.0a7+-4fe1c4b | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 148 ms: 1.02x slower                                                                   |
| float          | 48.3 ms                                                     | 50.9 ms: 1.05x slower                                                                  |
| nbody          | 57.8 ms                                                     | 68.3 ms: 1.18x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230415-pythonperf1-amd64-python-main-3.12.0a7+-4fe1c4b | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_v8       | 14.0 ms                                                     | 14.1 ms: 1.01x slower                                                                  |
| regex_compile  | 80.9 ms                                                     | 82.1 ms: 1.01x slower                                                                  |
| regex_effbot   | 1.56 ms                                                     | 1.60 ms: 1.02x slower                                                                  |
| regex_dna      | 119 ms                                                      | 123 ms: 1.03x slower                                                                   |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230415-pythonperf1-amd64-python-main-3.12.0a7+-4fe1c4b | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pickle_dict          | 18.6 us                                                     | 18.3 us: 1.02x faster                                                                  |
| xml_etree_parse      | 89.2 ms                                                     | 88.1 ms: 1.01x faster                                                                  |
| xml_etree_generate   | 52.7 ms                                                     | 52.4 ms: 1.01x faster                                                                  |
| pickle               | 6.68 us                                                     | 6.82 us: 1.02x slower                                                                  |
| json_loads           | 12.7 us                                                     | 13.0 us: 1.02x slower                                                                  |
| pickle_pure_python   | 183 us                                                      | 188 us: 1.03x slower                                                                   |
| unpickle_pure_python | 127 us                                                      | 132 us: 1.04x slower                                                                   |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                                           |

Benchmark hidden because not significant (6): pickle_list, xml_etree_iterparse, json_dumps, xml_etree_process, unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230415-pythonperf1-amd64-python-main-3.12.0a7+-4fe1c4b | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_xml     | 31.5 ms                                                     | 31.9 ms: 1.01x slower                                                                  |
| mako           | 6.53 ms                                                     | 6.62 ms: 1.01x slower                                                                  |
| genshi_text    | 14.3 ms                                                     | 14.9 ms: 1.04x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20230415-pythonperf1-amd64-python-main-3.12.0a7+-4fe1c4b | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| coroutines              | 13.9 ms                                                     | 13.4 ms: 1.04x faster                                                                  |
| logging_format          | 6.78 us                                                     | 6.58 us: 1.03x faster                                                                  |
| coverage                | 52.1 ms                                                     | 50.6 ms: 1.03x faster                                                                  |
| async_tree_memoization  | 360 ms                                                      | 350 ms: 1.03x faster                                                                   |
| go                      | 88.8 ms                                                     | 86.2 ms: 1.03x faster                                                                  |
| mdp                     | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                                 |
| gc_traversal            | 1.46 ms                                                     | 1.43 ms: 1.02x faster                                                                  |
| pickle_dict             | 18.6 us                                                     | 18.3 us: 1.02x faster                                                                  |
| async_tree_cpu_io_mixed | 478 ms                                                      | 471 ms: 1.01x faster                                                                   |
| logging_silent          | 59.7 ns                                                     | 58.9 ns: 1.01x faster                                                                  |
| pathlib                 | 82.3 ms                                                     | 81.2 ms: 1.01x faster                                                                  |
| xml_etree_parse         | 89.2 ms                                                     | 88.1 ms: 1.01x faster                                                                  |
| logging_simple          | 6.27 us                                                     | 6.20 us: 1.01x faster                                                                  |
| nqueens                 | 58.4 ms                                                     | 57.8 ms: 1.01x faster                                                                  |
| scimark_lu              | 54.8 ms                                                     | 54.3 ms: 1.01x faster                                                                  |
| chaos                   | 42.8 ms                                                     | 42.5 ms: 1.01x faster                                                                  |
| xml_etree_generate      | 52.7 ms                                                     | 52.4 ms: 1.01x faster                                                                  |
| spectral_norm           | 60.7 ms                                                     | 60.5 ms: 1.00x faster                                                                  |
| thrift                  | 471 us                                                      | 473 us: 1.00x slower                                                                   |
| regex_v8                | 14.0 ms                                                     | 14.1 ms: 1.01x slower                                                                  |
| deltablue               | 2.15 ms                                                     | 2.17 ms: 1.01x slower                                                                  |
| pprint_safe_repr        | 480 ms                                                      | 484 ms: 1.01x slower                                                                   |
| sympy_sum               | 93.7 ms                                                     | 94.7 ms: 1.01x slower                                                                  |
| async_tree_io           | 749 ms                                                      | 759 ms: 1.01x slower                                                                   |
| genshi_xml              | 31.5 ms                                                     | 31.9 ms: 1.01x slower                                                                  |
| create_gc_cycles        | 677 us                                                      | 686 us: 1.01x slower                                                                   |
| crypto_pyaes            | 45.3 ms                                                     | 45.9 ms: 1.01x slower                                                                  |
| mako                    | 6.53 ms                                                     | 6.62 ms: 1.01x slower                                                                  |
| telco                   | 3.76 ms                                                     | 3.82 ms: 1.01x slower                                                                  |
| pprint_pformat          | 985 ms                                                      | 999 ms: 1.01x slower                                                                   |
| regex_compile           | 80.9 ms                                                     | 82.1 ms: 1.01x slower                                                                  |
| dulwich_log             | 40.3 ms                                                     | 40.9 ms: 1.02x slower                                                                  |
| sympy_expand            | 269 ms                                                      | 274 ms: 1.02x slower                                                                   |
| dask                    | 352 ms                                                      | 358 ms: 1.02x slower                                                                   |
| pidigits                | 146 ms                                                      | 148 ms: 1.02x slower                                                                   |
| pickle                  | 6.68 us                                                     | 6.82 us: 1.02x slower                                                                  |
| sqlglot_normalize       | 172 ms                                                      | 176 ms: 1.02x slower                                                                   |
| comprehensions          | 14.5 us                                                     | 14.8 us: 1.02x slower                                                                  |
| json                    | 2.68 ms                                                     | 2.74 ms: 1.02x slower                                                                  |
| richards                | 25.9 ms                                                     | 26.5 ms: 1.02x slower                                                                  |
| regex_effbot            | 1.56 ms                                                     | 1.60 ms: 1.02x slower                                                                  |
| json_loads              | 12.7 us                                                     | 13.0 us: 1.02x slower                                                                  |
| bench_thread_pool       | 789 us                                                      | 809 us: 1.02x slower                                                                   |
| pickle_pure_python      | 183 us                                                      | 188 us: 1.03x slower                                                                   |
| async_generators        | 211 ms                                                      | 217 ms: 1.03x slower                                                                   |
| deepcopy_reduce         | 1.91 us                                                     | 1.96 us: 1.03x slower                                                                  |
| html5lib                | 35.4 ms                                                     | 36.4 ms: 1.03x slower                                                                  |
| regex_dna               | 119 ms                                                      | 123 ms: 1.03x slower                                                                   |
| 2to3                    | 198 ms                                                      | 204 ms: 1.03x slower                                                                   |
| sqlglot_optimize        | 31.3 ms                                                     | 32.2 ms: 1.03x slower                                                                  |
| bench_mp_pool           | 64.4 ms                                                     | 66.3 ms: 1.03x slower                                                                  |
| pycparser               | 639 ms                                                      | 659 ms: 1.03x slower                                                                   |
| sympy_integrate         | 12.7 ms                                                     | 13.1 ms: 1.03x slower                                                                  |
| scimark_sparse_mat_mult | 2.24 ms                                                     | 2.31 ms: 1.03x slower                                                                  |
| deepcopy_memo           | 22.0 us                                                     | 22.9 us: 1.04x slower                                                                  |
| tornado_http            | 85.4 ms                                                     | 88.8 ms: 1.04x slower                                                                  |
| genshi_text             | 14.3 ms                                                     | 14.9 ms: 1.04x slower                                                                  |
| sqlglot_parse           | 755 us                                                      | 787 us: 1.04x slower                                                                   |
| mypy2                   | 206 ms                                                      | 214 ms: 1.04x slower                                                                   |
| unpickle_pure_python    | 127 us                                                      | 132 us: 1.04x slower                                                                   |
| deepcopy                | 219 us                                                      | 228 us: 1.04x slower                                                                   |
| chameleon               | 4.67 ms                                                     | 4.88 ms: 1.04x slower                                                                  |
| docutils                | 1.49 sec                                                    | 1.56 sec: 1.05x slower                                                                 |
| scimark_monte_carlo     | 40.1 ms                                                     | 42.1 ms: 1.05x slower                                                                  |
| float                   | 48.3 ms                                                     | 50.9 ms: 1.05x slower                                                                  |
| raytrace                | 173 ms                                                      | 182 ms: 1.06x slower                                                                   |
| sqlglot_transpile       | 930 us                                                      | 988 us: 1.06x slower                                                                   |
| meteor_contest          | 71.2 ms                                                     | 76.2 ms: 1.07x slower                                                                  |
| generators              | 20.0 ms                                                     | 21.5 ms: 1.07x slower                                                                  |
| scimark_fft             | 157 ms                                                      | 170 ms: 1.08x slower                                                                   |
| scimark_sor             | 72.5 ms                                                     | 79.0 ms: 1.09x slower                                                                  |
| unpack_sequence         | 32.8 ns                                                     | 38.4 ns: 1.17x slower                                                                  |
| nbody                   | 57.8 ms                                                     | 68.3 ms: 1.18x slower                                                                  |
| Geometric mean          | (ref)                                                       | 1.02x slower                                                                           |

Benchmark hidden because not significant (17): pickle_list, python_startup_no_site, sqlite_synth, pyflate, xml_etree_iterparse, django_template, hexiom, async_tree_none, sympy_str, json_dumps, fannkuch, xml_etree_process, python_startup, unpickle_list, asyncio_tcp, unpickle, pylint
