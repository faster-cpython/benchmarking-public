
# Results vs. base

- fork: ericsnowcurrently
- ref: tstate_current_as_th
- machine: windows-amd64
- commit hash: 2332a2e
- commit date: 2023-04-07
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 202 ms                                                                      | 209 ms: 1.04x slower                                                                   |
| chameleon      | 4.75 ms                                                                     | 4.71 ms: 1.01x faster                                                                  |
| docutils       | 1.57 sec                                                                    | 1.60 sec: 1.02x slower                                                                 |
| html5lib       | 36.4 ms                                                                     | 37.4 ms: 1.03x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                                      | 146 ms: 1.01x faster                                                                   |
| float          | 48.6 ms                                                                     | 50.2 ms: 1.03x slower                                                                  |
| nbody          | 57.8 ms                                                                     | 62.0 ms: 1.07x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.03x slower                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 1.56 ms                                                                     | 1.54 ms: 1.01x faster                                                                  |
| regex_dna      | 117 ms                                                                      | 120 ms: 1.02x slower                                                                   |
| regex_v8       | 13.8 ms                                                                     | 14.1 ms: 1.02x slower                                                                  |
| regex_compile  | 82.3 ms                                                                     | 86.5 ms: 1.05x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|---------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| xml_etree_process   | 36.8 ms                                                                     | 36.3 ms: 1.01x faster                                                                  |
| xml_etree_generate  | 51.9 ms                                                                     | 52.8 ms: 1.02x slower                                                                  |
| unpickle_list       | 2.77 us                                                                     | 2.82 us: 1.02x slower                                                                  |
| json_loads          | 12.8 us                                                                     | 13.1 us: 1.03x slower                                                                  |
| json_dumps          | 5.36 ms                                                                     | 5.51 ms: 1.03x slower                                                                  |
| pickle_dict         | 19.1 us                                                                     | 19.6 us: 1.03x slower                                                                  |
| xml_etree_parse     | 90.9 ms                                                                     | 94.2 ms: 1.04x slower                                                                  |
| pickle_pure_python  | 176 us                                                                      | 182 us: 1.04x slower                                                                   |
| unpickle            | 8.10 us                                                                     | 8.43 us: 1.04x slower                                                                  |
| pickle_list         | 2.78 us                                                                     | 2.93 us: 1.05x slower                                                                  |
| pickle              | 6.97 us                                                                     | 7.39 us: 1.06x slower                                                                  |
| xml_etree_iterparse | 60.9 ms                                                                     | 65.3 ms: 1.07x slower                                                                  |
| Geometric mean      | (ref)                                                                       | 1.03x slower                                                                           |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_xml      | 30.8 ms                                                                     | 31.1 ms: 1.01x slower                                                                  |
| django_template | 21.7 ms                                                                     | 22.0 ms: 1.02x slower                                                                  |
| genshi_text     | 13.7 ms                                                                     | 14.2 ms: 1.03x slower                                                                  |
| mako            | 6.15 ms                                                                     | 6.38 ms: 1.04x slower                                                                  |
| Geometric mean  | (ref)                                                                       | 1.02x slower                                                                           |

All benchmarks:
===============

| Benchmark               | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| sqlite_synth            | 1.85 us                                                                     | 1.73 us: 1.07x faster                                                                  |
| sqlglot_parse           | 773 us                                                                      | 757 us: 1.02x faster                                                                   |
| create_gc_cycles        | 702 us                                                                      | 692 us: 1.02x faster                                                                   |
| pidigits                | 148 ms                                                                      | 146 ms: 1.01x faster                                                                   |
| xml_etree_process       | 36.8 ms                                                                     | 36.3 ms: 1.01x faster                                                                  |
| regex_effbot            | 1.56 ms                                                                     | 1.54 ms: 1.01x faster                                                                  |
| chameleon               | 4.75 ms                                                                     | 4.71 ms: 1.01x faster                                                                  |
| nqueens                 | 60.3 ms                                                                     | 59.9 ms: 1.01x faster                                                                  |
| spectral_norm           | 59.8 ms                                                                     | 59.5 ms: 1.00x faster                                                                  |
| deepcopy_memo           | 22.2 us                                                                     | 22.4 us: 1.01x slower                                                                  |
| logging_simple          | 6.20 us                                                                     | 6.25 us: 1.01x slower                                                                  |
| genshi_xml              | 30.8 ms                                                                     | 31.1 ms: 1.01x slower                                                                  |
| sqlglot_transpile       | 964 us                                                                      | 974 us: 1.01x slower                                                                   |
| bench_mp_pool           | 66.9 ms                                                                     | 67.6 ms: 1.01x slower                                                                  |
| sympy_expand            | 280 ms                                                                      | 283 ms: 1.01x slower                                                                   |
| mdp                     | 1.37 sec                                                                    | 1.39 sec: 1.01x slower                                                                 |
| dask                    | 358 ms                                                                      | 364 ms: 1.02x slower                                                                   |
| logging_format          | 6.52 us                                                                     | 6.63 us: 1.02x slower                                                                  |
| sympy_integrate         | 13.3 ms                                                                     | 13.6 ms: 1.02x slower                                                                  |
| scimark_monte_carlo     | 41.2 ms                                                                     | 41.9 ms: 1.02x slower                                                                  |
| xml_etree_generate      | 51.9 ms                                                                     | 52.8 ms: 1.02x slower                                                                  |
| unpickle_list           | 2.77 us                                                                     | 2.82 us: 1.02x slower                                                                  |
| django_template         | 21.7 ms                                                                     | 22.0 ms: 1.02x slower                                                                  |
| deltablue               | 1.97 ms                                                                     | 2.01 ms: 1.02x slower                                                                  |
| docutils                | 1.57 sec                                                                    | 1.60 sec: 1.02x slower                                                                 |
| pycparser               | 657 ms                                                                      | 670 ms: 1.02x slower                                                                   |
| sympy_str               | 175 ms                                                                      | 178 ms: 1.02x slower                                                                   |
| bench_thread_pool       | 845 us                                                                      | 861 us: 1.02x slower                                                                   |
| async_tree_io           | 762 ms                                                                      | 778 ms: 1.02x slower                                                                   |
| pyflate                 | 285 ms                                                                      | 291 ms: 1.02x slower                                                                   |
| dulwich_log             | 42.6 ms                                                                     | 43.6 ms: 1.02x slower                                                                  |
| regex_dna               | 117 ms                                                                      | 120 ms: 1.02x slower                                                                   |
| regex_v8                | 13.8 ms                                                                     | 14.1 ms: 1.02x slower                                                                  |
| sympy_sum               | 98.5 ms                                                                     | 101 ms: 1.03x slower                                                                   |
| pathlib                 | 86.6 ms                                                                     | 88.8 ms: 1.03x slower                                                                  |
| generators              | 20.9 ms                                                                     | 21.5 ms: 1.03x slower                                                                  |
| html5lib                | 36.4 ms                                                                     | 37.4 ms: 1.03x slower                                                                  |
| json_loads              | 12.8 us                                                                     | 13.1 us: 1.03x slower                                                                  |
| json_dumps              | 5.36 ms                                                                     | 5.51 ms: 1.03x slower                                                                  |
| go                      | 83.9 ms                                                                     | 86.3 ms: 1.03x slower                                                                  |
| mypy2                   | 218 ms                                                                      | 225 ms: 1.03x slower                                                                   |
| pickle_dict             | 19.1 us                                                                     | 19.6 us: 1.03x slower                                                                  |
| scimark_lu              | 53.9 ms                                                                     | 55.6 ms: 1.03x slower                                                                  |
| meteor_contest          | 72.1 ms                                                                     | 74.4 ms: 1.03x slower                                                                  |
| logging_silent          | 55.8 ns                                                                     | 57.6 ns: 1.03x slower                                                                  |
| float                   | 48.6 ms                                                                     | 50.2 ms: 1.03x slower                                                                  |
| raytrace                | 178 ms                                                                      | 184 ms: 1.03x slower                                                                   |
| genshi_text             | 13.7 ms                                                                     | 14.2 ms: 1.03x slower                                                                  |
| 2to3                    | 202 ms                                                                      | 209 ms: 1.04x slower                                                                   |
| xml_etree_parse         | 90.9 ms                                                                     | 94.2 ms: 1.04x slower                                                                  |
| async_generators        | 213 ms                                                                      | 221 ms: 1.04x slower                                                                   |
| pickle_pure_python      | 176 us                                                                      | 182 us: 1.04x slower                                                                   |
| sqlglot_optimize        | 31.3 ms                                                                     | 32.5 ms: 1.04x slower                                                                  |
| mako                    | 6.15 ms                                                                     | 6.38 ms: 1.04x slower                                                                  |
| thrift                  | 469 us                                                                      | 488 us: 1.04x slower                                                                   |
| sqlglot_normalize       | 171 ms                                                                      | 178 ms: 1.04x slower                                                                   |
| unpickle                | 8.10 us                                                                     | 8.43 us: 1.04x slower                                                                  |
| scimark_fft             | 162 ms                                                                      | 169 ms: 1.05x slower                                                                   |
| async_tree_none         | 302 ms                                                                      | 317 ms: 1.05x slower                                                                   |
| scimark_sor             | 73.1 ms                                                                     | 76.6 ms: 1.05x slower                                                                  |
| regex_compile           | 82.3 ms                                                                     | 86.5 ms: 1.05x slower                                                                  |
| richards                | 25.5 ms                                                                     | 26.8 ms: 1.05x slower                                                                  |
| pickle_list             | 2.78 us                                                                     | 2.93 us: 1.05x slower                                                                  |
| hexiom                  | 3.86 ms                                                                     | 4.06 ms: 1.05x slower                                                                  |
| pickle                  | 6.97 us                                                                     | 7.39 us: 1.06x slower                                                                  |
| deepcopy                | 215 us                                                                      | 229 us: 1.06x slower                                                                   |
| fannkuch                | 235 ms                                                                      | 250 ms: 1.06x slower                                                                   |
| deepcopy_reduce         | 1.90 us                                                                     | 2.02 us: 1.07x slower                                                                  |
| scimark_sparse_mat_mult | 2.13 ms                                                                     | 2.28 ms: 1.07x slower                                                                  |
| chaos                   | 41.2 ms                                                                     | 44.1 ms: 1.07x slower                                                                  |
| xml_etree_iterparse     | 60.9 ms                                                                     | 65.3 ms: 1.07x slower                                                                  |
| nbody                   | 57.8 ms                                                                     | 62.0 ms: 1.07x slower                                                                  |
| comprehensions          | 13.9 us                                                                     | 15.1 us: 1.08x slower                                                                  |
| coroutines              | 13.8 ms                                                                     | 15.4 ms: 1.12x slower                                                                  |
| Geometric mean          | (ref)                                                                       | 1.02x slower                                                                           |

Benchmark hidden because not significant (15): unpack_sequence, coverage, unpickle_pure_python, telco, gc_traversal, async_tree_cpu_io_mixed, crypto_pyaes, pprint_safe_repr, python_startup_no_site, json, pprint_pformat, python_startup, tornado_http, async_tree_memoization, asyncio_tcp
