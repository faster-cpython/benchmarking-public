
# Results vs. 3.11.0

- fork: faster-cpython
- ref: nogil_latest
- machine: windows-amd64
- commit hash: 1d39009
- commit date: 2023-04-16
- overall geometric mean: 1.05x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 224 ms: 1.07x slower                                                         |
| chameleon      | 5.11 ms                                                     | 5.66 ms: 1.11x slower                                                        |
| docutils       | 1.60 sec                                                    | 1.89 sec: 1.18x slower                                                       |
| html5lib       | 37.5 ms                                                     | 39.3 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.10x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 49.6 ms: 1.10x faster                                                        |
| pidigits       | 148 ms                                                      | 141 ms: 1.05x faster                                                         |
| nbody          | 70.0 ms                                                     | 89.9 ms: 1.28x slower                                                        |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                     | 13.2 ms: 1.05x faster                                                        |
| regex_dna      | 115 ms                                                      | 110 ms: 1.05x faster                                                         |
| regex_effbot   | 1.50 ms                                                     | 1.53 ms: 1.02x slower                                                        |
| regex_compile  | 90.6 ms                                                     | 96.4 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 6.50 ms: 1.16x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 82.9 ms: 1.16x faster                                                        |
| pickle_list          | 2.68 us                                                     | 2.81 us: 1.05x slower                                                        |
| unpickle_pure_python | 152 us                                                      | 159 us: 1.05x slower                                                         |
| pickle               | 6.61 us                                                     | 7.14 us: 1.08x slower                                                        |
| pickle_pure_python   | 200 us                                                      | 218 us: 1.09x slower                                                         |
| xml_etree_generate   | 52.2 ms                                                     | 57.5 ms: 1.10x slower                                                        |
| unpickle_list        | 2.55 us                                                     | 2.86 us: 1.12x slower                                                        |
| xml_etree_process    | 37.1 ms                                                     | 41.7 ms: 1.12x slower                                                        |
| json_loads           | 12.9 us                                                     | 14.6 us: 1.13x slower                                                        |
| unpickle             | 8.09 us                                                     | 9.19 us: 1.14x slower                                                        |
| pickle_dict          | 18.5 us                                                     | 21.8 us: 1.18x slower                                                        |
| xml_etree_iterparse  | 62.6 ms                                                     | 74.7 ms: 1.19x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                                        |
| python_startup         | 18.7 ms                                                     | 18.2 ms: 1.03x faster                                                        |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 37.3 ms                                                     | 35.3 ms: 1.06x faster                                                        |
| genshi_text     | 17.0 ms                                                     | 17.7 ms: 1.04x slower                                                        |
| django_template | 24.1 ms                                                     | 25.5 ms: 1.06x slower                                                        |
| mako            | 7.26 ms                                                     | 8.95 ms: 1.23x slower                                                        |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 779 ms                                                      | 405 ms: 1.92x faster                                                         |
| async_tree_none         | 320 ms                                                      | 189 ms: 1.69x faster                                                         |
| async_tree_memoization  | 371 ms                                                      | 240 ms: 1.54x faster                                                         |
| asyncio_tcp             | 699 ms                                                      | 489 ms: 1.43x faster                                                         |
| async_tree_cpu_io_mixed | 501 ms                                                      | 371 ms: 1.35x faster                                                         |
| sqlite_synth            | 1.68 us                                                     | 1.35 us: 1.24x faster                                                        |
| json_dumps              | 7.56 ms                                                     | 6.50 ms: 1.16x faster                                                        |
| xml_etree_parse         | 95.9 ms                                                     | 82.9 ms: 1.16x faster                                                        |
| json                    | 3.25 ms                                                     | 2.94 ms: 1.11x faster                                                        |
| float                   | 54.6 ms                                                     | 49.6 ms: 1.10x faster                                                        |
| genshi_xml              | 37.3 ms                                                     | 35.3 ms: 1.06x faster                                                        |
| pidigits                | 148 ms                                                      | 141 ms: 1.05x faster                                                         |
| regex_v8                | 13.8 ms                                                     | 13.2 ms: 1.05x faster                                                        |
| regex_dna               | 115 ms                                                      | 110 ms: 1.05x faster                                                         |
| python_startup_no_site  | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                                        |
| python_startup          | 18.7 ms                                                     | 18.2 ms: 1.03x faster                                                        |
| mdp                     | 1.67 sec                                                    | 1.63 sec: 1.02x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 43.6 ms: 1.02x faster                                                        |
| pyflate                 | 304 ms                                                      | 302 ms: 1.01x faster                                                         |
| nqueens                 | 64.9 ms                                                     | 65.6 ms: 1.01x slower                                                        |
| bench_mp_pool           | 62.5 ms                                                     | 63.9 ms: 1.02x slower                                                        |
| regex_effbot            | 1.50 ms                                                     | 1.53 ms: 1.02x slower                                                        |
| pycparser               | 691 ms                                                      | 713 ms: 1.03x slower                                                         |
| pathlib                 | 71.4 ms                                                     | 73.6 ms: 1.03x slower                                                        |
| deltablue               | 2.61 ms                                                     | 2.71 ms: 1.04x slower                                                        |
| genshi_text             | 17.0 ms                                                     | 17.7 ms: 1.04x slower                                                        |
| sqlglot_normalize       | 190 ms                                                      | 199 ms: 1.04x slower                                                         |
| logging_simple          | 6.61 us                                                     | 6.92 us: 1.05x slower                                                        |
| pickle_list             | 2.68 us                                                     | 2.81 us: 1.05x slower                                                        |
| html5lib                | 37.5 ms                                                     | 39.3 ms: 1.05x slower                                                        |
| unpickle_pure_python    | 152 us                                                      | 159 us: 1.05x slower                                                         |
| sqlglot_optimize        | 34.9 ms                                                     | 36.8 ms: 1.05x slower                                                        |
| logging_format          | 7.01 us                                                     | 7.40 us: 1.06x slower                                                        |
| richards                | 30.6 ms                                                     | 32.3 ms: 1.06x slower                                                        |
| go                      | 97.3 ms                                                     | 103 ms: 1.06x slower                                                         |
| django_template         | 24.1 ms                                                     | 25.5 ms: 1.06x slower                                                        |
| regex_compile           | 90.6 ms                                                     | 96.4 ms: 1.06x slower                                                        |
| gc_traversal            | 1.46 ms                                                     | 1.56 ms: 1.07x slower                                                        |
| 2to3                    | 209 ms                                                      | 224 ms: 1.07x slower                                                         |
| coverage                | 55.9 ms                                                     | 59.9 ms: 1.07x slower                                                        |
| logging_silent          | 69.8 ns                                                     | 75.0 ns: 1.07x slower                                                        |
| sympy_integrate         | 13.8 ms                                                     | 14.8 ms: 1.07x slower                                                        |
| pickle                  | 6.61 us                                                     | 7.14 us: 1.08x slower                                                        |
| create_gc_cycles        | 693 us                                                      | 748 us: 1.08x slower                                                         |
| sympy_expand            | 295 ms                                                      | 320 ms: 1.08x slower                                                         |
| sympy_str               | 182 ms                                                      | 198 ms: 1.09x slower                                                         |
| pickle_pure_python      | 200 us                                                      | 218 us: 1.09x slower                                                         |
| hexiom                  | 4.55 ms                                                     | 4.97 ms: 1.09x slower                                                        |
| sympy_sum               | 99.9 ms                                                     | 109 ms: 1.09x slower                                                         |
| xml_etree_generate      | 52.2 ms                                                     | 57.5 ms: 1.10x slower                                                        |
| thrift                  | 491 us                                                      | 542 us: 1.10x slower                                                         |
| deepcopy                | 246 us                                                      | 272 us: 1.11x slower                                                         |
| chameleon               | 5.11 ms                                                     | 5.66 ms: 1.11x slower                                                        |
| crypto_pyaes            | 47.6 ms                                                     | 52.7 ms: 1.11x slower                                                        |
| generators              | 33.8 ms                                                     | 37.5 ms: 1.11x slower                                                        |
| unpickle_list           | 2.55 us                                                     | 2.86 us: 1.12x slower                                                        |
| xml_etree_process       | 37.1 ms                                                     | 41.7 ms: 1.12x slower                                                        |
| fannkuch                | 252 ms                                                      | 285 ms: 1.13x slower                                                         |
| telco                   | 3.90 ms                                                     | 4.41 ms: 1.13x slower                                                        |
| json_loads              | 12.9 us                                                     | 14.6 us: 1.13x slower                                                        |
| unpickle                | 8.09 us                                                     | 9.19 us: 1.14x slower                                                        |
| sqlglot_transpile       | 1.16 ms                                                     | 1.33 ms: 1.14x slower                                                        |
| chaos                   | 47.1 ms                                                     | 53.7 ms: 1.14x slower                                                        |
| pprint_safe_repr        | 512 ms                                                      | 586 ms: 1.14x slower                                                         |
| raytrace                | 211 ms                                                      | 241 ms: 1.15x slower                                                         |
| scimark_monte_carlo     | 44.6 ms                                                     | 51.2 ms: 1.15x slower                                                        |
| coroutines              | 14.6 ms                                                     | 16.8 ms: 1.15x slower                                                        |
| scimark_lu              | 63.5 ms                                                     | 73.1 ms: 1.15x slower                                                        |
| async_generators        | 178 ms                                                      | 205 ms: 1.16x slower                                                         |
| meteor_contest          | 74.7 ms                                                     | 86.5 ms: 1.16x slower                                                        |
| deepcopy_reduce         | 2.07 us                                                     | 2.40 us: 1.16x slower                                                        |
| spectral_norm           | 67.9 ms                                                     | 78.8 ms: 1.16x slower                                                        |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.98 ms: 1.16x slower                                                        |
| pprint_pformat          | 1.04 sec                                                    | 1.21 sec: 1.16x slower                                                       |
| deepcopy_memo           | 25.2 us                                                     | 29.5 us: 1.17x slower                                                        |
| sqlglot_parse           | 952 us                                                      | 1.12 ms: 1.18x slower                                                        |
| pickle_dict             | 18.5 us                                                     | 21.8 us: 1.18x slower                                                        |
| docutils                | 1.60 sec                                                    | 1.89 sec: 1.18x slower                                                       |
| scimark_sor             | 75.6 ms                                                     | 89.1 ms: 1.18x slower                                                        |
| xml_etree_iterparse     | 62.6 ms                                                     | 74.7 ms: 1.19x slower                                                        |
| comprehensions          | 15.9 us                                                     | 19.1 us: 1.20x slower                                                        |
| unpack_sequence         | 46.1 ns                                                     | 55.2 ns: 1.20x slower                                                        |
| bench_thread_pool       | 852 us                                                      | 1.03 ms: 1.21x slower                                                        |
| scimark_fft             | 178 ms                                                      | 220 ms: 1.23x slower                                                         |
| mako                    | 7.26 ms                                                     | 8.95 ms: 1.23x slower                                                        |
| mypy2                   | 229 ms                                                      | 291 ms: 1.27x slower                                                         |
| nbody                   | 70.0 ms                                                     | 89.9 ms: 1.28x slower                                                        |
| Geometric mean          | (ref)                                                       | 1.05x slower                                                                 |
Ignored benchmarks (11) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, dask, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x
