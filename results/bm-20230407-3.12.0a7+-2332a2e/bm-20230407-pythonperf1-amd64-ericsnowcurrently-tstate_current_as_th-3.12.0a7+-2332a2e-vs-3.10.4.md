
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: tstate_current_as_th
- machine: windows-amd64
- commit hash: 2332a2e
- commit date: 2023-04-07
- overall geometric mean: 1.18x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 209 ms: 1.13x faster                                                                   |
| chameleon      | 5.92 ms                                                     | 4.71 ms: 1.26x faster                                                                  |
| docutils       | 1.89 sec                                                    | 1.60 sec: 1.18x faster                                                                 |
| html5lib       | 46.5 ms                                                     | 37.4 ms: 1.24x faster                                                                  |
| tornado_http   | 109 ms                                                      | 86.8 ms: 1.26x faster                                                                  |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 50.2 ms: 1.20x faster                                                                  |
| nbody          | 69.3 ms                                                     | 62.0 ms: 1.12x faster                                                                  |
| pidigits       | 145 ms                                                      | 146 ms: 1.01x slower                                                                   |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 86.5 ms: 1.20x faster                                                                  |
| regex_dna      | 132 ms                                                      | 120 ms: 1.10x faster                                                                   |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                                  |
| regex_v8       | 15.0 ms                                                     | 14.1 ms: 1.07x faster                                                                  |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.51 ms: 1.54x faster                                                                  |
| pickle_pure_python   | 257 us                                                      | 182 us: 1.41x faster                                                                   |
| unpickle_pure_python | 171 us                                                      | 129 us: 1.33x faster                                                                   |
| xml_etree_process    | 43.4 ms                                                     | 36.3 ms: 1.20x faster                                                                  |
| unpickle             | 9.17 us                                                     | 8.43 us: 1.09x faster                                                                  |
| xml_etree_parse      | 102 ms                                                      | 94.2 ms: 1.08x faster                                                                  |
| json_loads           | 14.2 us                                                     | 13.1 us: 1.08x faster                                                                  |
| xml_etree_generate   | 54.5 ms                                                     | 52.8 ms: 1.03x faster                                                                  |
| xml_etree_iterparse  | 63.5 ms                                                     | 65.3 ms: 1.03x slower                                                                  |
| pickle               | 6.80 us                                                     | 7.39 us: 1.09x slower                                                                  |
| pickle_list          | 2.59 us                                                     | 2.93 us: 1.13x slower                                                                  |
| pickle_dict          | 16.9 us                                                     | 19.6 us: 1.16x slower                                                                  |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.0 ms: 1.05x faster                                                                  |
| python_startup_no_site | 15.5 ms                                                     | 16.0 ms: 1.03x slower                                                                  |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.38 ms: 1.38x faster                                                                  |
| genshi_text     | 19.0 ms                                                     | 14.2 ms: 1.35x faster                                                                  |
| genshi_xml      | 40.5 ms                                                     | 31.1 ms: 1.30x faster                                                                  |
| django_template | 28.2 ms                                                     | 22.0 ms: 1.28x faster                                                                  |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.01 ms: 2.08x faster                                                                  |
| logging_silent          | 96.4 ns                                                     | 57.6 ns: 1.67x faster                                                                  |
| sqlglot_parse           | 1.22 ms                                                     | 757 us: 1.61x faster                                                                   |
| go                      | 136 ms                                                      | 86.3 ms: 1.58x faster                                                                  |
| mypy2                   | 352 ms                                                      | 225 ms: 1.56x faster                                                                   |
| json_dumps              | 8.50 ms                                                     | 5.51 ms: 1.54x faster                                                                  |
| richards                | 41.2 ms                                                     | 26.8 ms: 1.54x faster                                                                  |
| scimark_lu              | 85.4 ms                                                     | 55.6 ms: 1.54x faster                                                                  |
| sqlglot_transpile       | 1.46 ms                                                     | 974 us: 1.50x faster                                                                   |
| raytrace                | 271 ms                                                      | 184 ms: 1.48x faster                                                                   |
| generators              | 31.6 ms                                                     | 21.5 ms: 1.47x faster                                                                  |
| asyncio_tcp             | 712 ms                                                      | 489 ms: 1.46x faster                                                                   |
| pickle_pure_python      | 257 us                                                      | 182 us: 1.41x faster                                                                   |
| crypto_pyaes            | 62.3 ms                                                     | 45.0 ms: 1.38x faster                                                                  |
| unpack_sequence         | 37.8 ns                                                     | 27.3 ns: 1.38x faster                                                                  |
| mako                    | 8.80 ms                                                     | 6.38 ms: 1.38x faster                                                                  |
| async_tree_io           | 1.07 sec                                                    | 778 ms: 1.37x faster                                                                   |
| scimark_sor             | 105 ms                                                      | 76.6 ms: 1.37x faster                                                                  |
| async_tree_memoization  | 497 ms                                                      | 365 ms: 1.36x faster                                                                   |
| hexiom                  | 5.52 ms                                                     | 4.06 ms: 1.36x faster                                                                  |
| genshi_text             | 19.0 ms                                                     | 14.2 ms: 1.35x faster                                                                  |
| chaos                   | 58.9 ms                                                     | 44.1 ms: 1.34x faster                                                                  |
| scimark_monte_carlo     | 55.9 ms                                                     | 41.9 ms: 1.33x faster                                                                  |
| unpickle_pure_python    | 171 us                                                      | 129 us: 1.33x faster                                                                   |
| pyflate                 | 387 ms                                                      | 291 ms: 1.33x faster                                                                   |
| async_tree_none         | 420 ms                                                      | 317 ms: 1.33x faster                                                                   |
| spectral_norm           | 78.0 ms                                                     | 59.5 ms: 1.31x faster                                                                  |
| genshi_xml              | 40.5 ms                                                     | 31.1 ms: 1.30x faster                                                                  |
| pycparser               | 868 ms                                                      | 670 ms: 1.30x faster                                                                   |
| django_template         | 28.2 ms                                                     | 22.0 ms: 1.28x faster                                                                  |
| deepcopy_memo           | 28.5 us                                                     | 22.4 us: 1.27x faster                                                                  |
| async_tree_cpu_io_mixed | 609 ms                                                      | 482 ms: 1.26x faster                                                                   |
| thrift                  | 615 us                                                      | 488 us: 1.26x faster                                                                   |
| chameleon               | 5.92 ms                                                     | 4.71 ms: 1.26x faster                                                                  |
| tornado_http            | 109 ms                                                      | 86.8 ms: 1.26x faster                                                                  |
| html5lib                | 46.5 ms                                                     | 37.4 ms: 1.24x faster                                                                  |
| pprint_pformat          | 1.21 sec                                                    | 973 ms: 1.24x faster                                                                   |
| mdp                     | 1.71 sec                                                    | 1.39 sec: 1.23x faster                                                                 |
| pprint_safe_repr        | 589 ms                                                      | 479 ms: 1.23x faster                                                                   |
| sqlglot_optimize        | 39.0 ms                                                     | 32.5 ms: 1.20x faster                                                                  |
| float                   | 60.2 ms                                                     | 50.2 ms: 1.20x faster                                                                  |
| regex_compile           | 103 ms                                                      | 86.5 ms: 1.20x faster                                                                  |
| xml_etree_process       | 43.4 ms                                                     | 36.3 ms: 1.20x faster                                                                  |
| docutils                | 1.89 sec                                                    | 1.60 sec: 1.18x faster                                                                 |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.28 ms: 1.17x faster                                                                  |
| scimark_fft             | 193 ms                                                      | 169 ms: 1.14x faster                                                                   |
| sqlglot_normalize       | 202 ms                                                      | 178 ms: 1.14x faster                                                                   |
| 2to3                    | 237 ms                                                      | 209 ms: 1.13x faster                                                                   |
| create_gc_cycles        | 782 us                                                      | 692 us: 1.13x faster                                                                   |
| nqueens                 | 67.0 ms                                                     | 59.9 ms: 1.12x faster                                                                  |
| nbody                   | 69.3 ms                                                     | 62.0 ms: 1.12x faster                                                                  |
| deepcopy                | 255 us                                                      | 229 us: 1.12x faster                                                                   |
| json                    | 3.05 ms                                                     | 2.73 ms: 1.11x faster                                                                  |
| sympy_expand            | 315 ms                                                      | 283 ms: 1.11x faster                                                                   |
| regex_dna               | 132 ms                                                      | 120 ms: 1.10x faster                                                                   |
| bench_thread_pool       | 946 us                                                      | 861 us: 1.10x faster                                                                   |
| sympy_integrate         | 14.8 ms                                                     | 13.6 ms: 1.09x faster                                                                  |
| dulwich_log             | 47.6 ms                                                     | 43.6 ms: 1.09x faster                                                                  |
| unpickle                | 9.17 us                                                     | 8.43 us: 1.09x faster                                                                  |
| xml_etree_parse         | 102 ms                                                      | 94.2 ms: 1.08x faster                                                                  |
| regex_effbot            | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                                  |
| json_loads              | 14.2 us                                                     | 13.1 us: 1.08x faster                                                                  |
| deepcopy_reduce         | 2.16 us                                                     | 2.02 us: 1.07x faster                                                                  |
| regex_v8                | 15.0 ms                                                     | 14.1 ms: 1.07x faster                                                                  |
| sqlite_synth            | 1.84 us                                                     | 1.73 us: 1.06x faster                                                                  |
| comprehensions          | 16.0 us                                                     | 15.1 us: 1.06x faster                                                                  |
| sympy_str               | 188 ms                                                      | 178 ms: 1.06x faster                                                                   |
| python_startup          | 20.0 ms                                                     | 19.0 ms: 1.05x faster                                                                  |
| xml_etree_generate      | 54.5 ms                                                     | 52.8 ms: 1.03x faster                                                                  |
| coroutines              | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                                                  |
| fannkuch                | 258 ms                                                      | 250 ms: 1.03x faster                                                                   |
| sympy_sum               | 104 ms                                                      | 101 ms: 1.03x faster                                                                   |
| async_generators        | 224 ms                                                      | 221 ms: 1.01x faster                                                                   |
| pidigits                | 145 ms                                                      | 146 ms: 1.01x slower                                                                   |
| logging_simple          | 6.20 us                                                     | 6.25 us: 1.01x slower                                                                  |
| telco                   | 3.78 ms                                                     | 3.88 ms: 1.03x slower                                                                  |
| meteor_contest          | 72.5 ms                                                     | 74.4 ms: 1.03x slower                                                                  |
| xml_etree_iterparse     | 63.5 ms                                                     | 65.3 ms: 1.03x slower                                                                  |
| python_startup_no_site  | 15.5 ms                                                     | 16.0 ms: 1.03x slower                                                                  |
| pickle                  | 6.80 us                                                     | 7.39 us: 1.09x slower                                                                  |
| gc_traversal            | 1.34 ms                                                     | 1.49 ms: 1.11x slower                                                                  |
| bench_mp_pool           | 60.7 ms                                                     | 67.6 ms: 1.11x slower                                                                  |
| pickle_list             | 2.59 us                                                     | 2.93 us: 1.13x slower                                                                  |
| pathlib                 | 77.4 ms                                                     | 88.8 ms: 1.15x slower                                                                  |
| pickle_dict             | 16.9 us                                                     | 19.6 us: 1.16x slower                                                                  |
| dask                    | 305 ms                                                      | 364 ms: 1.19x slower                                                                   |
| coverage                | 40.0 ms                                                     | 52.7 ms: 1.32x slower                                                                  |
| Geometric mean          | (ref)                                                       | 1.18x faster                                                                           |

Benchmark hidden because not significant (2): logging_format, unpickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.12x
