
# Results vs. 3.11.0

- fork: python
- ref: f9774e57d84162ff0cba
- machine: windows-amd64
- commit hash: f9774e5
- commit date: 2023-03-07
- overall geometric mean: 1.08x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 194 ms: 1.08x faster                                                       |
| chameleon      | 5.11 ms                                                     | 4.76 ms: 1.07x faster                                                      |
| docutils       | 1.60 sec                                                    | 1.51 sec: 1.06x faster                                                     |
| html5lib       | 37.5 ms                                                     | 34.8 ms: 1.08x faster                                                      |
| tornado_http   | 91.8 ms                                                     | 90.6 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 47.4 ms: 1.15x faster                                                      |
| nbody          | 70.0 ms                                                     | 63.3 ms: 1.11x faster                                                      |
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 83.5 ms: 1.09x faster                                                      |
| regex_v8       | 13.8 ms                                                     | 13.4 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.51 ms: 1.37x faster                                                      |
| unpickle_pure_python | 152 us                                                      | 124 us: 1.23x faster                                                       |
| pickle_pure_python   | 200 us                                                      | 175 us: 1.14x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 88.4 ms: 1.09x faster                                                      |
| xml_etree_process    | 37.1 ms                                                     | 35.6 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 61.3 ms: 1.02x faster                                                      |
| unpickle             | 8.09 us                                                     | 7.98 us: 1.01x faster                                                      |
| json_loads           | 12.9 us                                                     | 13.4 us: 1.04x slower                                                      |
| pickle_list          | 2.68 us                                                     | 2.80 us: 1.05x slower                                                      |
| pickle               | 6.61 us                                                     | 6.96 us: 1.05x slower                                                      |
| unpickle_list        | 2.55 us                                                     | 2.74 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_generate, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.5 ms: 1.03x faster                                                      |
| python_startup         | 18.7 ms                                                     | 18.2 ms: 1.03x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.9 ms: 1.22x faster                                                      |
| genshi_xml      | 37.3 ms                                                     | 30.9 ms: 1.21x faster                                                      |
| mako            | 7.26 ms                                                     | 6.20 ms: 1.17x faster                                                      |
| django_template | 24.1 ms                                                     | 20.9 ms: 1.15x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 27.9 ns: 1.65x faster                                                      |
| generators              | 33.8 ms                                                     | 21.9 ms: 1.54x faster                                                      |
| asyncio_tcp             | 699 ms                                                      | 463 ms: 1.51x faster                                                       |
| json_dumps              | 7.56 ms                                                     | 5.51 ms: 1.37x faster                                                      |
| deltablue               | 2.61 ms                                                     | 1.92 ms: 1.36x faster                                                      |
| richards                | 30.6 ms                                                     | 24.5 ms: 1.25x faster                                                      |
| logging_silent          | 69.8 ns                                                     | 56.5 ns: 1.24x faster                                                      |
| unpickle_pure_python    | 152 us                                                      | 124 us: 1.23x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 13.9 ms: 1.22x faster                                                      |
| genshi_xml              | 37.3 ms                                                     | 30.9 ms: 1.21x faster                                                      |
| hexiom                  | 4.55 ms                                                     | 3.83 ms: 1.19x faster                                                      |
| json                    | 3.25 ms                                                     | 2.74 ms: 1.19x faster                                                      |
| go                      | 97.3 ms                                                     | 82.6 ms: 1.18x faster                                                      |
| mako                    | 7.26 ms                                                     | 6.20 ms: 1.17x faster                                                      |
| fannkuch                | 252 ms                                                      | 216 ms: 1.17x faster                                                       |
| raytrace                | 211 ms                                                      | 180 ms: 1.17x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                     |
| django_template         | 24.1 ms                                                     | 20.9 ms: 1.15x faster                                                      |
| float                   | 54.6 ms                                                     | 47.4 ms: 1.15x faster                                                      |
| pickle_pure_python      | 200 us                                                      | 175 us: 1.14x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 56.9 ms: 1.14x faster                                                      |
| sqlglot_normalize       | 190 ms                                                      | 168 ms: 1.13x faster                                                       |
| pyflate                 | 304 ms                                                      | 270 ms: 1.13x faster                                                       |
| chaos                   | 47.1 ms                                                     | 42.0 ms: 1.12x faster                                                      |
| deepcopy                | 246 us                                                      | 219 us: 1.12x faster                                                       |
| coverage                | 55.9 ms                                                     | 49.9 ms: 1.12x faster                                                      |
| sqlglot_optimize        | 34.9 ms                                                     | 31.2 ms: 1.12x faster                                                      |
| deepcopy_memo           | 25.2 us                                                     | 22.6 us: 1.12x faster                                                      |
| nbody                   | 70.0 ms                                                     | 63.3 ms: 1.11x faster                                                      |
| scimark_monte_carlo     | 44.6 ms                                                     | 40.4 ms: 1.11x faster                                                      |
| deepcopy_reduce         | 2.07 us                                                     | 1.88 us: 1.10x faster                                                      |
| meteor_contest          | 74.7 ms                                                     | 68.0 ms: 1.10x faster                                                      |
| crypto_pyaes            | 47.6 ms                                                     | 43.3 ms: 1.10x faster                                                      |
| sqlglot_transpile       | 1.16 ms                                                     | 1.06 ms: 1.10x faster                                                      |
| sqlglot_parse           | 952 us                                                      | 871 us: 1.09x faster                                                       |
| mypy2                   | 229 ms                                                      | 211 ms: 1.09x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 83.5 ms: 1.09x faster                                                      |
| xml_etree_parse         | 95.9 ms                                                     | 88.4 ms: 1.09x faster                                                      |
| logging_simple          | 6.61 us                                                     | 6.10 us: 1.08x faster                                                      |
| scimark_lu              | 63.5 ms                                                     | 58.7 ms: 1.08x faster                                                      |
| html5lib                | 37.5 ms                                                     | 34.8 ms: 1.08x faster                                                      |
| 2to3                    | 209 ms                                                      | 194 ms: 1.08x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.76 ms: 1.07x faster                                                      |
| logging_format          | 7.01 us                                                     | 6.55 us: 1.07x faster                                                      |
| pprint_safe_repr        | 512 ms                                                      | 478 ms: 1.07x faster                                                       |
| sympy_expand            | 295 ms                                                      | 277 ms: 1.07x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 977 ms: 1.06x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.51 sec: 1.06x faster                                                     |
| scimark_fft             | 178 ms                                                      | 169 ms: 1.06x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 13.1 ms: 1.06x faster                                                      |
| scimark_sor             | 75.6 ms                                                     | 71.6 ms: 1.06x faster                                                      |
| sympy_str               | 182 ms                                                      | 173 ms: 1.05x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 42.2 ms: 1.05x faster                                                      |
| async_tree_none         | 320 ms                                                      | 304 ms: 1.05x faster                                                       |
| coroutines              | 14.6 ms                                                     | 14.0 ms: 1.05x faster                                                      |
| async_tree_io           | 779 ms                                                      | 744 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed | 501 ms                                                      | 479 ms: 1.05x faster                                                       |
| pycparser               | 691 ms                                                      | 663 ms: 1.04x faster                                                       |
| async_tree_memoization  | 371 ms                                                      | 356 ms: 1.04x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 35.6 ms: 1.04x faster                                                      |
| regex_v8                | 13.8 ms                                                     | 13.4 ms: 1.04x faster                                                      |
| sympy_sum               | 99.9 ms                                                     | 96.6 ms: 1.03x faster                                                      |
| create_gc_cycles        | 693 us                                                      | 671 us: 1.03x faster                                                       |
| bench_thread_pool       | 852 us                                                      | 827 us: 1.03x faster                                                       |
| thrift                  | 491 us                                                      | 476 us: 1.03x faster                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 15.5 ms: 1.03x faster                                                      |
| python_startup          | 18.7 ms                                                     | 18.2 ms: 1.03x faster                                                      |
| xml_etree_iterparse     | 62.6 ms                                                     | 61.3 ms: 1.02x faster                                                      |
| unpickle                | 8.09 us                                                     | 7.98 us: 1.01x faster                                                      |
| tornado_http            | 91.8 ms                                                     | 90.6 ms: 1.01x faster                                                      |
| telco                   | 3.90 ms                                                     | 3.86 ms: 1.01x faster                                                      |
| gc_traversal            | 1.46 ms                                                     | 1.44 ms: 1.01x faster                                                      |
| spectral_norm           | 67.9 ms                                                     | 67.2 ms: 1.01x faster                                                      |
| pidigits                | 148 ms                                                      | 147 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.56 ms: 1.00x faster                                                      |
| bench_mp_pool           | 62.5 ms                                                     | 63.1 ms: 1.01x slower                                                      |
| pathlib                 | 71.4 ms                                                     | 73.9 ms: 1.04x slower                                                      |
| json_loads              | 12.9 us                                                     | 13.4 us: 1.04x slower                                                      |
| pickle_list             | 2.68 us                                                     | 2.80 us: 1.05x slower                                                      |
| pickle                  | 6.61 us                                                     | 6.96 us: 1.05x slower                                                      |
| sqlite_synth            | 1.68 us                                                     | 1.79 us: 1.06x slower                                                      |
| unpickle_list           | 2.55 us                                                     | 2.74 us: 1.08x slower                                                      |
| async_generators        | 178 ms                                                      | 223 ms: 1.26x slower                                                       |
| dask                    | 264 ms                                                      | 352 ms: 1.33x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (5): xml_etree_generate, comprehensions, regex_dna, regex_effbot, pickle_dict
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x
