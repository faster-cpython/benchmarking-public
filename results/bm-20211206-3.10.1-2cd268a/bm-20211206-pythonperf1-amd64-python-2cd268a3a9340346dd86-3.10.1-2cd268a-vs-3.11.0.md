
# Results vs. 3.11.0

- fork: python
- ref: 2cd268a3a9340346dd86
- machine: windows-amd64
- commit hash: 2cd268a
- commit date: 2021-12-06
- overall geometric mean: 1.12x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211206-pythonperf1-amd64-python-2cd268a3a9340346dd86-3.10.1-2cd268a |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 232 ms: 1.11x slower                                                     |
| chameleon      | 5.11 ms                                                     | 5.89 ms: 1.15x slower                                                    |
| docutils       | 1.60 sec                                                    | 1.88 sec: 1.17x slower                                                   |
| html5lib       | 37.5 ms                                                     | 48.7 ms: 1.30x slower                                                    |
| tornado_http   | 91.8 ms                                                     | 109 ms: 1.19x slower                                                     |
| Geometric mean | (ref)                                                       | 1.18x slower                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211206-pythonperf1-amd64-python-2cd268a3a9340346dd86-3.10.1-2cd268a |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                     |
| nbody          | 70.0 ms                                                     | 77.2 ms: 1.10x slower                                                    |
| float          | 54.6 ms                                                     | 61.8 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                       | 1.08x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211206-pythonperf1-amd64-python-2cd268a3a9340346dd86-3.10.1-2cd268a |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                     | 15.0 ms: 1.08x slower                                                    |
| regex_dna      | 115 ms                                                      | 129 ms: 1.12x slower                                                     |
| regex_compile  | 90.6 ms                                                     | 103 ms: 1.14x slower                                                     |
| regex_effbot   | 1.50 ms                                                     | 1.74 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                       | 1.13x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211206-pythonperf1-amd64-python-2cd268a3a9340346dd86-3.10.1-2cd268a |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_dict          | 18.5 us                                                     | 17.0 us: 1.09x faster                                                    |
| unpickle             | 8.09 us                                                     | 8.17 us: 1.01x slower                                                    |
| xml_etree_parse      | 95.9 ms                                                     | 98.0 ms: 1.02x slower                                                    |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.6 ms: 1.03x slower                                                    |
| pickle               | 6.61 us                                                     | 6.84 us: 1.04x slower                                                    |
| unpickle_list        | 2.55 us                                                     | 2.64 us: 1.04x slower                                                    |
| xml_etree_generate   | 52.2 ms                                                     | 55.0 ms: 1.05x slower                                                    |
| json_dumps           | 7.56 ms                                                     | 8.45 ms: 1.12x slower                                                    |
| json_loads           | 12.9 us                                                     | 15.0 us: 1.16x slower                                                    |
| unpickle_pure_python | 152 us                                                      | 177 us: 1.17x slower                                                     |
| xml_etree_process    | 37.1 ms                                                     | 44.0 ms: 1.19x slower                                                    |
| pickle_pure_python   | 200 us                                                      | 267 us: 1.33x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                             |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211206-pythonperf1-amd64-python-2cd268a3a9340346dd86-3.10.1-2cd268a |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.1 ms: 1.05x faster                                                    |
| python_startup         | 18.7 ms                                                     | 19.7 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                       | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211206-pythonperf1-amd64-python-2cd268a3a9340346dd86-3.10.1-2cd268a |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 37.3 ms                                                     | 40.9 ms: 1.10x slower                                                    |
| genshi_text     | 17.0 ms                                                     | 19.6 ms: 1.15x slower                                                    |
| mako            | 7.26 ms                                                     | 8.56 ms: 1.18x slower                                                    |
| django_template | 24.1 ms                                                     | 29.2 ms: 1.21x slower                                                    |
| Geometric mean  | (ref)                                                       | 1.16x slower                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211206-pythonperf1-amd64-python-2cd268a3a9340346dd86-3.10.1-2cd268a |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| coverage                | 55.9 ms                                                     | 38.8 ms: 1.44x faster                                                    |
| unpack_sequence         | 46.1 ns                                                     | 40.5 ns: 1.14x faster                                                    |
| generators              | 33.8 ms                                                     | 30.7 ms: 1.10x faster                                                    |
| pickle_dict             | 18.5 us                                                     | 17.0 us: 1.09x faster                                                    |
| gc_traversal            | 1.46 ms                                                     | 1.37 ms: 1.06x faster                                                    |
| logging_simple          | 6.61 us                                                     | 6.24 us: 1.06x faster                                                    |
| python_startup_no_site  | 15.9 ms                                                     | 15.1 ms: 1.05x faster                                                    |
| logging_format          | 7.01 us                                                     | 6.72 us: 1.04x faster                                                    |
| bench_mp_pool           | 62.5 ms                                                     | 60.4 ms: 1.03x faster                                                    |
| meteor_contest          | 74.7 ms                                                     | 73.2 ms: 1.02x faster                                                    |
| telco                   | 3.90 ms                                                     | 3.86 ms: 1.01x faster                                                    |
| pidigits                | 148 ms                                                      | 149 ms: 1.01x slower                                                     |
| nqueens                 | 64.9 ms                                                     | 65.5 ms: 1.01x slower                                                    |
| unpickle                | 8.09 us                                                     | 8.17 us: 1.01x slower                                                    |
| xml_etree_parse         | 95.9 ms                                                     | 98.0 ms: 1.02x slower                                                    |
| mdp                     | 1.67 sec                                                    | 1.72 sec: 1.03x slower                                                   |
| xml_etree_iterparse     | 62.6 ms                                                     | 64.6 ms: 1.03x slower                                                    |
| pickle                  | 6.61 us                                                     | 6.84 us: 1.04x slower                                                    |
| deepcopy                | 246 us                                                      | 254 us: 1.04x slower                                                     |
| unpickle_list           | 2.55 us                                                     | 2.64 us: 1.04x slower                                                    |
| deepcopy_reduce         | 2.07 us                                                     | 2.15 us: 1.04x slower                                                    |
| sympy_sum               | 99.9 ms                                                     | 104 ms: 1.04x slower                                                     |
| sympy_str               | 182 ms                                                      | 191 ms: 1.05x slower                                                     |
| pylint                  | 326 ms                                                      | 343 ms: 1.05x slower                                                     |
| xml_etree_generate      | 52.2 ms                                                     | 55.0 ms: 1.05x slower                                                    |
| python_startup          | 18.7 ms                                                     | 19.7 ms: 1.05x slower                                                    |
| fannkuch                | 252 ms                                                      | 266 ms: 1.05x slower                                                     |
| pathlib                 | 71.4 ms                                                     | 75.9 ms: 1.06x slower                                                    |
| sqlglot_normalize       | 190 ms                                                      | 203 ms: 1.07x slower                                                     |
| sympy_expand            | 295 ms                                                      | 316 ms: 1.07x slower                                                     |
| sympy_integrate         | 13.8 ms                                                     | 14.9 ms: 1.08x slower                                                    |
| regex_v8                | 13.8 ms                                                     | 15.0 ms: 1.08x slower                                                    |
| coroutines              | 14.6 ms                                                     | 15.9 ms: 1.09x slower                                                    |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.80 ms: 1.09x slower                                                    |
| scimark_fft             | 178 ms                                                      | 195 ms: 1.09x slower                                                     |
| dulwich_log             | 44.5 ms                                                     | 48.7 ms: 1.09x slower                                                    |
| genshi_xml              | 37.3 ms                                                     | 40.9 ms: 1.10x slower                                                    |
| sqlite_synth            | 1.68 us                                                     | 1.85 us: 1.10x slower                                                    |
| aiohttp                 | 899 us                                                      | 990 us: 1.10x slower                                                     |
| nbody                   | 70.0 ms                                                     | 77.2 ms: 1.10x slower                                                    |
| create_gc_cycles        | 693 us                                                      | 770 us: 1.11x slower                                                     |
| 2to3                    | 209 ms                                                      | 232 ms: 1.11x slower                                                     |
| sqlalchemy_imperative   | 10.2 ms                                                     | 11.4 ms: 1.12x slower                                                    |
| json_dumps              | 7.56 ms                                                     | 8.45 ms: 1.12x slower                                                    |
| regex_dna               | 115 ms                                                      | 129 ms: 1.12x slower                                                     |
| sqlglot_optimize        | 34.9 ms                                                     | 39.2 ms: 1.12x slower                                                    |
| float                   | 54.6 ms                                                     | 61.8 ms: 1.13x slower                                                    |
| bench_thread_pool       | 852 us                                                      | 965 us: 1.13x slower                                                     |
| regex_compile           | 90.6 ms                                                     | 103 ms: 1.14x slower                                                     |
| deepcopy_memo           | 25.2 us                                                     | 28.7 us: 1.14x slower                                                    |
| chameleon               | 5.11 ms                                                     | 5.89 ms: 1.15x slower                                                    |
| genshi_text             | 17.0 ms                                                     | 19.6 ms: 1.15x slower                                                    |
| regex_effbot            | 1.50 ms                                                     | 1.74 ms: 1.16x slower                                                    |
| json_loads              | 12.9 us                                                     | 15.0 us: 1.16x slower                                                    |
| unpickle_pure_python    | 152 us                                                      | 177 us: 1.17x slower                                                     |
| spectral_norm           | 67.9 ms                                                     | 79.4 ms: 1.17x slower                                                    |
| docutils                | 1.60 sec                                                    | 1.88 sec: 1.17x slower                                                   |
| pprint_safe_repr        | 512 ms                                                      | 601 ms: 1.17x slower                                                     |
| mako                    | 7.26 ms                                                     | 8.56 ms: 1.18x slower                                                    |
| xml_etree_process       | 37.1 ms                                                     | 44.0 ms: 1.19x slower                                                    |
| tornado_http            | 91.8 ms                                                     | 109 ms: 1.19x slower                                                     |
| hexiom                  | 4.55 ms                                                     | 5.42 ms: 1.19x slower                                                    |
| pprint_pformat          | 1.04 sec                                                    | 1.24 sec: 1.20x slower                                                   |
| dask                    | 264 ms                                                      | 319 ms: 1.21x slower                                                     |
| sqlalchemy_declarative  | 81.5 ms                                                     | 98.4 ms: 1.21x slower                                                    |
| django_template         | 24.1 ms                                                     | 29.2 ms: 1.21x slower                                                    |
| async_tree_cpu_io_mixed | 501 ms                                                      | 615 ms: 1.23x slower                                                     |
| pycparser               | 691 ms                                                      | 861 ms: 1.25x slower                                                     |
| sqlglot_transpile       | 1.16 ms                                                     | 1.45 ms: 1.25x slower                                                    |
| async_generators        | 178 ms                                                      | 224 ms: 1.26x slower                                                     |
| chaos                   | 47.1 ms                                                     | 59.4 ms: 1.26x slower                                                    |
| sqlglot_parse           | 952 us                                                      | 1.21 ms: 1.27x slower                                                    |
| thrift                  | 491 us                                                      | 625 us: 1.27x slower                                                     |
| scimark_monte_carlo     | 44.6 ms                                                     | 56.9 ms: 1.27x slower                                                    |
| raytrace                | 211 ms                                                      | 273 ms: 1.29x slower                                                     |
| html5lib                | 37.5 ms                                                     | 48.7 ms: 1.30x slower                                                    |
| pyflate                 | 304 ms                                                      | 394 ms: 1.30x slower                                                     |
| async_tree_none         | 320 ms                                                      | 417 ms: 1.30x slower                                                     |
| async_tree_memoization  | 371 ms                                                      | 484 ms: 1.30x slower                                                     |
| scimark_lu              | 63.5 ms                                                     | 83.4 ms: 1.31x slower                                                    |
| async_tree_io           | 779 ms                                                      | 1.03 sec: 1.32x slower                                                   |
| pickle_pure_python      | 200 us                                                      | 267 us: 1.33x slower                                                     |
| richards                | 30.6 ms                                                     | 40.9 ms: 1.34x slower                                                    |
| crypto_pyaes            | 47.6 ms                                                     | 65.5 ms: 1.38x slower                                                    |
| scimark_sor             | 75.6 ms                                                     | 106 ms: 1.40x slower                                                     |
| logging_silent          | 69.8 ns                                                     | 98.0 ns: 1.40x slower                                                    |
| go                      | 97.3 ms                                                     | 137 ms: 1.41x slower                                                     |
| mypy2                   | 229 ms                                                      | 340 ms: 1.48x slower                                                     |
| deltablue               | 2.61 ms                                                     | 4.13 ms: 1.58x slower                                                    |
| Geometric mean          | (ref)                                                       | 1.12x slower                                                             |

Benchmark hidden because not significant (5): json, comprehensions, flaskblogging, pickle_list, asyncio_tcp
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.09x
