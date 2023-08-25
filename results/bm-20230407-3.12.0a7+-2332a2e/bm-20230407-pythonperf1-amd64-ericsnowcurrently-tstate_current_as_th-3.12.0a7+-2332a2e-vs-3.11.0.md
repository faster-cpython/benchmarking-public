
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: tstate_current_as_th
- machine: windows-amd64
- commit hash: 2332a2e
- commit date: 2023-04-07
- overall geometric mean: 1.06x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| chameleon      | 5.11 ms                                                     | 4.71 ms: 1.09x faster                                                                  |
| tornado_http   | 91.8 ms                                                     | 86.8 ms: 1.06x faster                                                                  |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                           |

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 62.0 ms: 1.13x faster                                                                  |
| float          | 54.6 ms                                                     | 50.2 ms: 1.09x faster                                                                  |
| pidigits       | 148 ms                                                      | 146 ms: 1.01x faster                                                                   |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 86.5 ms: 1.05x faster                                                                  |
| regex_v8       | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                                                  |
| regex_effbot   | 1.50 ms                                                     | 1.54 ms: 1.03x slower                                                                  |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                                   |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.51 ms: 1.37x faster                                                                  |
| unpickle_pure_python | 152 us                                                      | 129 us: 1.18x faster                                                                   |
| pickle_pure_python   | 200 us                                                      | 182 us: 1.10x faster                                                                   |
| xml_etree_process    | 37.1 ms                                                     | 36.3 ms: 1.02x faster                                                                  |
| xml_etree_parse      | 95.9 ms                                                     | 94.2 ms: 1.02x faster                                                                  |
| xml_etree_generate   | 52.2 ms                                                     | 52.8 ms: 1.01x slower                                                                  |
| json_loads           | 12.9 us                                                     | 13.1 us: 1.02x slower                                                                  |
| unpickle             | 8.09 us                                                     | 8.43 us: 1.04x slower                                                                  |
| xml_etree_iterparse  | 62.6 ms                                                     | 65.3 ms: 1.04x slower                                                                  |
| pickle_dict          | 18.5 us                                                     | 19.6 us: 1.06x slower                                                                  |
| pickle_list          | 2.68 us                                                     | 2.93 us: 1.09x slower                                                                  |
| unpickle_list        | 2.55 us                                                     | 2.82 us: 1.11x slower                                                                  |
| pickle               | 6.61 us                                                     | 7.39 us: 1.12x slower                                                                  |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup | 18.7 ms                                                     | 19.0 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_xml      | 37.3 ms                                                     | 31.1 ms: 1.20x faster                                                                  |
| genshi_text     | 17.0 ms                                                     | 14.2 ms: 1.20x faster                                                                  |
| mako            | 7.26 ms                                                     | 6.38 ms: 1.14x faster                                                                  |
| django_template | 24.1 ms                                                     | 22.0 ms: 1.09x faster                                                                  |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 27.3 ns: 1.68x faster                                                                  |
| generators              | 33.8 ms                                                     | 21.5 ms: 1.57x faster                                                                  |
| asyncio_tcp             | 699 ms                                                      | 489 ms: 1.43x faster                                                                   |
| json_dumps              | 7.56 ms                                                     | 5.51 ms: 1.37x faster                                                                  |
| deltablue               | 2.61 ms                                                     | 2.01 ms: 1.30x faster                                                                  |
| sqlglot_parse           | 952 us                                                      | 757 us: 1.26x faster                                                                   |
| logging_silent          | 69.8 ns                                                     | 57.6 ns: 1.21x faster                                                                  |
| mdp                     | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                                 |
| genshi_xml              | 37.3 ms                                                     | 31.1 ms: 1.20x faster                                                                  |
| genshi_text             | 17.0 ms                                                     | 14.2 ms: 1.20x faster                                                                  |
| sqlglot_transpile       | 1.16 ms                                                     | 974 us: 1.19x faster                                                                   |
| json                    | 3.25 ms                                                     | 2.73 ms: 1.19x faster                                                                  |
| unpickle_pure_python    | 152 us                                                      | 129 us: 1.18x faster                                                                   |
| raytrace                | 211 ms                                                      | 184 ms: 1.15x faster                                                                   |
| scimark_lu              | 63.5 ms                                                     | 55.6 ms: 1.14x faster                                                                  |
| richards                | 30.6 ms                                                     | 26.8 ms: 1.14x faster                                                                  |
| spectral_norm           | 67.9 ms                                                     | 59.5 ms: 1.14x faster                                                                  |
| mako                    | 7.26 ms                                                     | 6.38 ms: 1.14x faster                                                                  |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.28 ms: 1.13x faster                                                                  |
| nbody                   | 70.0 ms                                                     | 62.0 ms: 1.13x faster                                                                  |
| go                      | 97.3 ms                                                     | 86.3 ms: 1.13x faster                                                                  |
| deepcopy_memo           | 25.2 us                                                     | 22.4 us: 1.12x faster                                                                  |
| hexiom                  | 4.55 ms                                                     | 4.06 ms: 1.12x faster                                                                  |
| pickle_pure_python      | 200 us                                                      | 182 us: 1.10x faster                                                                   |
| django_template         | 24.1 ms                                                     | 22.0 ms: 1.09x faster                                                                  |
| float                   | 54.6 ms                                                     | 50.2 ms: 1.09x faster                                                                  |
| chameleon               | 5.11 ms                                                     | 4.71 ms: 1.09x faster                                                                  |
| nqueens                 | 64.9 ms                                                     | 59.9 ms: 1.08x faster                                                                  |
| deepcopy                | 246 us                                                      | 229 us: 1.07x faster                                                                   |
| sqlglot_optimize        | 34.9 ms                                                     | 32.5 ms: 1.07x faster                                                                  |
| sqlglot_normalize       | 190 ms                                                      | 178 ms: 1.07x faster                                                                   |
| chaos                   | 47.1 ms                                                     | 44.1 ms: 1.07x faster                                                                  |
| pprint_safe_repr        | 512 ms                                                      | 479 ms: 1.07x faster                                                                   |
| pprint_pformat          | 1.04 sec                                                    | 973 ms: 1.07x faster                                                                   |
| scimark_monte_carlo     | 44.6 ms                                                     | 41.9 ms: 1.06x faster                                                                  |
| coverage                | 55.9 ms                                                     | 52.7 ms: 1.06x faster                                                                  |
| logging_simple          | 6.61 us                                                     | 6.25 us: 1.06x faster                                                                  |
| logging_format          | 7.01 us                                                     | 6.63 us: 1.06x faster                                                                  |
| tornado_http            | 91.8 ms                                                     | 86.8 ms: 1.06x faster                                                                  |
| crypto_pyaes            | 47.6 ms                                                     | 45.0 ms: 1.06x faster                                                                  |
| scimark_fft             | 178 ms                                                      | 169 ms: 1.06x faster                                                                   |
| comprehensions          | 15.9 us                                                     | 15.1 us: 1.06x faster                                                                  |
| regex_compile           | 90.6 ms                                                     | 86.5 ms: 1.05x faster                                                                  |
| pyflate                 | 304 ms                                                      | 291 ms: 1.04x faster                                                                   |
| sympy_expand            | 295 ms                                                      | 283 ms: 1.04x faster                                                                   |
| async_tree_cpu_io_mixed | 501 ms                                                      | 482 ms: 1.04x faster                                                                   |
| pycparser               | 691 ms                                                      | 670 ms: 1.03x faster                                                                   |
| deepcopy_reduce         | 2.07 us                                                     | 2.02 us: 1.03x faster                                                                  |
| sympy_str               | 182 ms                                                      | 178 ms: 1.02x faster                                                                   |
| xml_etree_process       | 37.1 ms                                                     | 36.3 ms: 1.02x faster                                                                  |
| dulwich_log             | 44.5 ms                                                     | 43.6 ms: 1.02x faster                                                                  |
| xml_etree_parse         | 95.9 ms                                                     | 94.2 ms: 1.02x faster                                                                  |
| mypy2                   | 229 ms                                                      | 225 ms: 1.02x faster                                                                   |
| sympy_integrate         | 13.8 ms                                                     | 13.6 ms: 1.02x faster                                                                  |
| pidigits                | 148 ms                                                      | 146 ms: 1.01x faster                                                                   |
| async_tree_none         | 320 ms                                                      | 317 ms: 1.01x faster                                                                   |
| telco                   | 3.90 ms                                                     | 3.88 ms: 1.01x faster                                                                  |
| meteor_contest          | 74.7 ms                                                     | 74.4 ms: 1.00x faster                                                                  |
| xml_etree_generate      | 52.2 ms                                                     | 52.8 ms: 1.01x slower                                                                  |
| bench_thread_pool       | 852 us                                                      | 861 us: 1.01x slower                                                                   |
| sympy_sum               | 99.9 ms                                                     | 101 ms: 1.01x slower                                                                   |
| scimark_sor             | 75.6 ms                                                     | 76.6 ms: 1.01x slower                                                                  |
| python_startup          | 18.7 ms                                                     | 19.0 ms: 1.01x slower                                                                  |
| json_loads              | 12.9 us                                                     | 13.1 us: 1.02x slower                                                                  |
| regex_v8                | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                                                  |
| gc_traversal            | 1.46 ms                                                     | 1.49 ms: 1.02x slower                                                                  |
| sqlite_synth            | 1.68 us                                                     | 1.73 us: 1.03x slower                                                                  |
| regex_effbot            | 1.50 ms                                                     | 1.54 ms: 1.03x slower                                                                  |
| regex_dna               | 115 ms                                                      | 120 ms: 1.04x slower                                                                   |
| unpickle                | 8.09 us                                                     | 8.43 us: 1.04x slower                                                                  |
| xml_etree_iterparse     | 62.6 ms                                                     | 65.3 ms: 1.04x slower                                                                  |
| coroutines              | 14.6 ms                                                     | 15.4 ms: 1.05x slower                                                                  |
| pickle_dict             | 18.5 us                                                     | 19.6 us: 1.06x slower                                                                  |
| bench_mp_pool           | 62.5 ms                                                     | 67.6 ms: 1.08x slower                                                                  |
| pickle_list             | 2.68 us                                                     | 2.93 us: 1.09x slower                                                                  |
| unpickle_list           | 2.55 us                                                     | 2.82 us: 1.11x slower                                                                  |
| pickle                  | 6.61 us                                                     | 7.39 us: 1.12x slower                                                                  |
| pathlib                 | 71.4 ms                                                     | 88.8 ms: 1.24x slower                                                                  |
| async_generators        | 178 ms                                                      | 221 ms: 1.24x slower                                                                   |
| dask                    | 264 ms                                                      | 364 ms: 1.38x slower                                                                   |
| Geometric mean          | (ref)                                                       | 1.06x faster                                                                           |

Benchmark hidden because not significant (9): async_tree_memoization, fannkuch, thrift, html5lib, create_gc_cycles, async_tree_io, 2to3, docutils, python_startup_no_site
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
