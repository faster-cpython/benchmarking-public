
# Results vs. 3.11.0

- fork: python
- ref: 7d4cc5aa854fdea4d01a
- machine: windows-amd64
- commit hash: 7d4cc5a
- commit date: 2023-04-04
- overall geometric mean: 1.12x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf1-amd64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 233 ms: 1.11x slower                                                      |
| chameleon      | 5.11 ms                                                     | 5.67 ms: 1.11x slower                                                     |
| docutils       | 1.60 sec                                                    | 1.82 sec: 1.14x slower                                                    |
| html5lib       | 37.5 ms                                                     | 45.8 ms: 1.22x slower                                                     |
| tornado_http   | 91.8 ms                                                     | 108 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.15x slower                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf1-amd64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                                      |
| nbody          | 70.0 ms                                                     | 75.5 ms: 1.08x slower                                                     |
| float          | 54.6 ms                                                     | 60.7 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                       | 1.06x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf1-amd64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                     | 14.6 ms: 1.06x slower                                                     |
| regex_effbot   | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                     |
| regex_dna      | 115 ms                                                      | 129 ms: 1.12x slower                                                      |
| regex_compile  | 90.6 ms                                                     | 102 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf1-amd64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_iterparse  | 62.6 ms                                                     | 63.4 ms: 1.01x slower                                                     |
| xml_etree_generate   | 52.2 ms                                                     | 54.3 ms: 1.04x slower                                                     |
| unpickle_list        | 2.55 us                                                     | 2.66 us: 1.04x slower                                                     |
| json_loads           | 12.9 us                                                     | 13.7 us: 1.06x slower                                                     |
| pickle_list          | 2.68 us                                                     | 2.86 us: 1.07x slower                                                     |
| pickle               | 6.61 us                                                     | 7.34 us: 1.11x slower                                                     |
| unpickle             | 8.09 us                                                     | 9.30 us: 1.15x slower                                                     |
| unpickle_pure_python | 152 us                                                      | 177 us: 1.17x slower                                                      |
| xml_etree_process    | 37.1 ms                                                     | 43.5 ms: 1.17x slower                                                     |
| json_dumps           | 7.56 ms                                                     | 8.90 ms: 1.18x slower                                                     |
| pickle_pure_python   | 200 us                                                      | 266 us: 1.33x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                              |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf1-amd64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.6 ms: 1.02x faster                                                     |
| python_startup         | 18.7 ms                                                     | 21.1 ms: 1.13x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf1-amd64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 37.3 ms                                                     | 39.1 ms: 1.05x slower                                                     |
| genshi_text     | 17.0 ms                                                     | 18.8 ms: 1.11x slower                                                     |
| django_template | 24.1 ms                                                     | 28.9 ms: 1.20x slower                                                     |
| mako            | 7.26 ms                                                     | 8.76 ms: 1.21x slower                                                     |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                              |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf1-amd64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coverage                | 55.9 ms                                                     | 39.2 ms: 1.43x faster                                                     |
| unpack_sequence         | 46.1 ns                                                     | 42.1 ns: 1.09x faster                                                     |
| json                    | 3.25 ms                                                     | 3.02 ms: 1.08x faster                                                     |
| logging_simple          | 6.61 us                                                     | 6.28 us: 1.05x faster                                                     |
| generators              | 33.8 ms                                                     | 32.1 ms: 1.05x faster                                                     |
| logging_format          | 7.01 us                                                     | 6.76 us: 1.04x faster                                                     |
| meteor_contest          | 74.7 ms                                                     | 72.1 ms: 1.04x faster                                                     |
| bench_mp_pool           | 62.5 ms                                                     | 60.4 ms: 1.04x faster                                                     |
| gc_traversal            | 1.46 ms                                                     | 1.42 ms: 1.03x faster                                                     |
| comprehensions          | 15.9 us                                                     | 15.6 us: 1.02x faster                                                     |
| python_startup_no_site  | 15.9 ms                                                     | 15.6 ms: 1.02x faster                                                     |
| pidigits                | 148 ms                                                      | 147 ms: 1.01x faster                                                      |
| flaskblogging           | 2.04 sec                                                    | 2.05 sec: 1.00x slower                                                    |
| telco                   | 3.90 ms                                                     | 3.93 ms: 1.01x slower                                                     |
| xml_etree_iterparse     | 62.6 ms                                                     | 63.4 ms: 1.01x slower                                                     |
| mdp                     | 1.67 sec                                                    | 1.71 sec: 1.03x slower                                                    |
| deepcopy_reduce         | 2.07 us                                                     | 2.13 us: 1.03x slower                                                     |
| sympy_str               | 182 ms                                                      | 188 ms: 1.04x slower                                                      |
| xml_etree_generate      | 52.2 ms                                                     | 54.3 ms: 1.04x slower                                                     |
| nqueens                 | 64.9 ms                                                     | 67.5 ms: 1.04x slower                                                     |
| pathlib                 | 71.4 ms                                                     | 74.4 ms: 1.04x slower                                                     |
| unpickle_list           | 2.55 us                                                     | 2.66 us: 1.04x slower                                                     |
| pylint                  | 326 ms                                                      | 341 ms: 1.05x slower                                                      |
| sympy_sum               | 99.9 ms                                                     | 105 ms: 1.05x slower                                                      |
| genshi_xml              | 37.3 ms                                                     | 39.1 ms: 1.05x slower                                                     |
| regex_v8                | 13.8 ms                                                     | 14.6 ms: 1.06x slower                                                     |
| sympy_expand            | 295 ms                                                      | 312 ms: 1.06x slower                                                      |
| sqlglot_normalize       | 190 ms                                                      | 202 ms: 1.06x slower                                                      |
| deepcopy                | 246 us                                                      | 260 us: 1.06x slower                                                      |
| json_loads              | 12.9 us                                                     | 13.7 us: 1.06x slower                                                     |
| pickle_list             | 2.68 us                                                     | 2.86 us: 1.07x slower                                                     |
| dulwich_log             | 44.5 ms                                                     | 47.6 ms: 1.07x slower                                                     |
| aiohttp                 | 899 us                                                      | 962 us: 1.07x slower                                                      |
| sympy_integrate         | 13.8 ms                                                     | 14.8 ms: 1.07x slower                                                     |
| coroutines              | 14.6 ms                                                     | 15.7 ms: 1.07x slower                                                     |
| regex_effbot            | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                     |
| nbody                   | 70.0 ms                                                     | 75.5 ms: 1.08x slower                                                     |
| asyncio_tcp             | 699 ms                                                      | 755 ms: 1.08x slower                                                      |
| bench_thread_pool       | 852 us                                                      | 928 us: 1.09x slower                                                      |
| sqlalchemy_imperative   | 10.2 ms                                                     | 11.1 ms: 1.09x slower                                                     |
| fannkuch                | 252 ms                                                      | 276 ms: 1.10x slower                                                      |
| sqlite_synth            | 1.68 us                                                     | 1.84 us: 1.10x slower                                                     |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.83 ms: 1.10x slower                                                     |
| sqlglot_optimize        | 34.9 ms                                                     | 38.5 ms: 1.10x slower                                                     |
| chameleon               | 5.11 ms                                                     | 5.67 ms: 1.11x slower                                                     |
| genshi_text             | 17.0 ms                                                     | 18.8 ms: 1.11x slower                                                     |
| float                   | 54.6 ms                                                     | 60.7 ms: 1.11x slower                                                     |
| pickle                  | 6.61 us                                                     | 7.34 us: 1.11x slower                                                     |
| 2to3                    | 209 ms                                                      | 233 ms: 1.11x slower                                                      |
| regex_dna               | 115 ms                                                      | 129 ms: 1.12x slower                                                      |
| create_gc_cycles        | 693 us                                                      | 777 us: 1.12x slower                                                      |
| python_startup          | 18.7 ms                                                     | 21.1 ms: 1.13x slower                                                     |
| regex_compile           | 90.6 ms                                                     | 102 ms: 1.13x slower                                                      |
| deepcopy_memo           | 25.2 us                                                     | 28.6 us: 1.13x slower                                                     |
| scimark_fft             | 178 ms                                                      | 203 ms: 1.14x slower                                                      |
| docutils                | 1.60 sec                                                    | 1.82 sec: 1.14x slower                                                    |
| pprint_safe_repr        | 512 ms                                                      | 584 ms: 1.14x slower                                                      |
| dask                    | 264 ms                                                      | 303 ms: 1.15x slower                                                      |
| unpickle                | 8.09 us                                                     | 9.30 us: 1.15x slower                                                     |
| pprint_pformat          | 1.04 sec                                                    | 1.19 sec: 1.15x slower                                                    |
| unpickle_pure_python    | 152 us                                                      | 177 us: 1.17x slower                                                      |
| xml_etree_process       | 37.1 ms                                                     | 43.5 ms: 1.17x slower                                                     |
| sqlalchemy_declarative  | 81.5 ms                                                     | 95.8 ms: 1.18x slower                                                     |
| tornado_http            | 91.8 ms                                                     | 108 ms: 1.18x slower                                                      |
| json_dumps              | 7.56 ms                                                     | 8.90 ms: 1.18x slower                                                     |
| hexiom                  | 4.55 ms                                                     | 5.40 ms: 1.19x slower                                                     |
| async_tree_cpu_io_mixed | 501 ms                                                      | 598 ms: 1.19x slower                                                      |
| spectral_norm           | 67.9 ms                                                     | 81.4 ms: 1.20x slower                                                     |
| django_template         | 24.1 ms                                                     | 28.9 ms: 1.20x slower                                                     |
| mako                    | 7.26 ms                                                     | 8.76 ms: 1.21x slower                                                     |
| pycparser               | 691 ms                                                      | 839 ms: 1.21x slower                                                      |
| html5lib                | 37.5 ms                                                     | 45.8 ms: 1.22x slower                                                     |
| sqlglot_transpile       | 1.16 ms                                                     | 1.42 ms: 1.22x slower                                                     |
| async_generators        | 178 ms                                                      | 218 ms: 1.23x slower                                                      |
| sqlglot_parse           | 952 us                                                      | 1.19 ms: 1.25x slower                                                     |
| chaos                   | 47.1 ms                                                     | 59.2 ms: 1.26x slower                                                     |
| thrift                  | 491 us                                                      | 629 us: 1.28x slower                                                      |
| raytrace                | 211 ms                                                      | 271 ms: 1.28x slower                                                      |
| pyflate                 | 304 ms                                                      | 391 ms: 1.29x slower                                                      |
| async_tree_none         | 320 ms                                                      | 414 ms: 1.29x slower                                                      |
| async_tree_memoization  | 371 ms                                                      | 481 ms: 1.30x slower                                                      |
| scimark_monte_carlo     | 44.6 ms                                                     | 58.9 ms: 1.32x slower                                                     |
| crypto_pyaes            | 47.6 ms                                                     | 63.2 ms: 1.33x slower                                                     |
| scimark_lu              | 63.5 ms                                                     | 84.5 ms: 1.33x slower                                                     |
| pickle_pure_python      | 200 us                                                      | 266 us: 1.33x slower                                                      |
| async_tree_io           | 779 ms                                                      | 1.04 sec: 1.33x slower                                                    |
| richards                | 30.6 ms                                                     | 40.9 ms: 1.34x slower                                                     |
| logging_silent          | 69.8 ns                                                     | 97.2 ns: 1.39x slower                                                     |
| go                      | 97.3 ms                                                     | 137 ms: 1.41x slower                                                      |
| scimark_sor             | 75.6 ms                                                     | 107 ms: 1.42x slower                                                      |
| mypy2                   | 229 ms                                                      | 343 ms: 1.50x slower                                                      |
| deltablue               | 2.61 ms                                                     | 4.11 ms: 1.57x slower                                                     |
| Geometric mean          | (ref)                                                       | 1.12x slower                                                              |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_dict
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x
