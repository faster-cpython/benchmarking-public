
# Results vs. 3.11.0

- fork: python
- ref: 7c12e4835ebe52287acd
- machine: windows-amd64
- commit hash: 7c12e48
- commit date: 2021-10-05
- overall geometric mean: 1.09x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211005-pythonperf1-amd64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 222 ms: 1.06x slower                                                       |
| chameleon      | 5.11 ms                                                     | 5.68 ms: 1.11x slower                                                      |
| docutils       | 1.60 sec                                                    | 1.73 sec: 1.08x slower                                                     |
| html5lib       | 37.5 ms                                                     | 41.5 ms: 1.11x slower                                                      |
| tornado_http   | 91.8 ms                                                     | 97.6 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211005-pythonperf1-amd64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| float          | 54.6 ms                                                     | 57.2 ms: 1.05x slower                                                      |
| nbody          | 70.0 ms                                                     | 86.8 ms: 1.24x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211005-pythonperf1-amd64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 92.3 ms: 1.02x slower                                                      |
| regex_v8       | 13.8 ms                                                     | 14.4 ms: 1.04x slower                                                      |
| regex_effbot   | 1.50 ms                                                     | 1.66 ms: 1.11x slower                                                      |
| regex_dna      | 115 ms                                                      | 129 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211005-pythonperf1-amd64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_dict          | 18.5 us                                                     | 16.8 us: 1.10x faster                                                      |
| pickle_list          | 2.68 us                                                     | 2.66 us: 1.01x faster                                                      |
| unpickle_list        | 2.55 us                                                     | 2.56 us: 1.01x slower                                                      |
| xml_etree_parse      | 95.9 ms                                                     | 98.4 ms: 1.03x slower                                                      |
| unpickle             | 8.09 us                                                     | 8.48 us: 1.05x slower                                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 65.6 ms: 1.05x slower                                                      |
| xml_etree_generate   | 52.2 ms                                                     | 54.8 ms: 1.05x slower                                                      |
| json_dumps           | 7.56 ms                                                     | 8.03 ms: 1.06x slower                                                      |
| xml_etree_process    | 37.1 ms                                                     | 40.3 ms: 1.09x slower                                                      |
| json_loads           | 12.9 us                                                     | 14.4 us: 1.12x slower                                                      |
| unpickle_pure_python | 152 us                                                      | 172 us: 1.13x slower                                                       |
| pickle_pure_python   | 200 us                                                      | 240 us: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211005-pythonperf1-amd64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.6 ms: 1.02x faster                                                      |
| python_startup         | 18.7 ms                                                     | 20.7 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211005-pythonperf1-amd64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 17.3 ms: 1.02x slower                                                      |
| django_template | 24.1 ms                                                     | 25.8 ms: 1.07x slower                                                      |
| mako            | 7.26 ms                                                     | 8.12 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211005-pythonperf1-amd64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| logging_simple          | 6.61 us                                                     | 5.24 us: 1.26x faster                                                      |
| logging_format          | 7.01 us                                                     | 5.64 us: 1.24x faster                                                      |
| generators              | 33.8 ms                                                     | 28.9 ms: 1.17x faster                                                      |
| asyncio_tcp             | 699 ms                                                      | 628 ms: 1.11x faster                                                       |
| unpack_sequence         | 46.1 ns                                                     | 41.7 ns: 1.11x faster                                                      |
| pickle_dict             | 18.5 us                                                     | 16.8 us: 1.10x faster                                                      |
| async_tree_none         | 320 ms                                                      | 296 ms: 1.08x faster                                                       |
| json                    | 3.25 ms                                                     | 3.01 ms: 1.08x faster                                                      |
| gc_traversal            | 1.46 ms                                                     | 1.37 ms: 1.06x faster                                                      |
| mdp                     | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                     |
| pylint                  | 326 ms                                                      | 318 ms: 1.02x faster                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 15.6 ms: 1.02x faster                                                      |
| pickle_list             | 2.68 us                                                     | 2.66 us: 1.01x faster                                                      |
| unpickle_list           | 2.55 us                                                     | 2.56 us: 1.01x slower                                                      |
| meteor_contest          | 74.7 ms                                                     | 75.3 ms: 1.01x slower                                                      |
| bench_mp_pool           | 62.5 ms                                                     | 63.0 ms: 1.01x slower                                                      |
| pidigits                | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| regex_compile           | 90.6 ms                                                     | 92.3 ms: 1.02x slower                                                      |
| telco                   | 3.90 ms                                                     | 3.98 ms: 1.02x slower                                                      |
| genshi_text             | 17.0 ms                                                     | 17.3 ms: 1.02x slower                                                      |
| xml_etree_parse         | 95.9 ms                                                     | 98.4 ms: 1.03x slower                                                      |
| pathlib                 | 71.4 ms                                                     | 73.4 ms: 1.03x slower                                                      |
| sympy_str               | 182 ms                                                      | 188 ms: 1.03x slower                                                       |
| async_tree_memoization  | 371 ms                                                      | 384 ms: 1.04x slower                                                       |
| dulwich_log             | 44.5 ms                                                     | 46.1 ms: 1.04x slower                                                      |
| regex_v8                | 13.8 ms                                                     | 14.4 ms: 1.04x slower                                                      |
| sympy_integrate         | 13.8 ms                                                     | 14.4 ms: 1.04x slower                                                      |
| deepcopy                | 246 us                                                      | 256 us: 1.04x slower                                                       |
| nqueens                 | 64.9 ms                                                     | 67.7 ms: 1.04x slower                                                      |
| deepcopy_reduce         | 2.07 us                                                     | 2.16 us: 1.04x slower                                                      |
| sympy_expand            | 295 ms                                                      | 309 ms: 1.05x slower                                                       |
| float                   | 54.6 ms                                                     | 57.2 ms: 1.05x slower                                                      |
| unpickle                | 8.09 us                                                     | 8.48 us: 1.05x slower                                                      |
| xml_etree_iterparse     | 62.6 ms                                                     | 65.6 ms: 1.05x slower                                                      |
| sqlalchemy_imperative   | 10.2 ms                                                     | 10.7 ms: 1.05x slower                                                      |
| xml_etree_generate      | 52.2 ms                                                     | 54.8 ms: 1.05x slower                                                      |
| sqlglot_normalize       | 190 ms                                                      | 201 ms: 1.05x slower                                                       |
| sqlalchemy_declarative  | 81.5 ms                                                     | 86.3 ms: 1.06x slower                                                      |
| tornado_http            | 91.8 ms                                                     | 97.6 ms: 1.06x slower                                                      |
| json_dumps              | 7.56 ms                                                     | 8.03 ms: 1.06x slower                                                      |
| 2to3                    | 209 ms                                                      | 222 ms: 1.06x slower                                                       |
| raytrace                | 211 ms                                                      | 224 ms: 1.06x slower                                                       |
| django_template         | 24.1 ms                                                     | 25.8 ms: 1.07x slower                                                      |
| sqlite_synth            | 1.68 us                                                     | 1.80 us: 1.07x slower                                                      |
| bench_thread_pool       | 852 us                                                      | 915 us: 1.07x slower                                                       |
| docutils                | 1.60 sec                                                    | 1.73 sec: 1.08x slower                                                     |
| async_tree_cpu_io_mixed | 501 ms                                                      | 541 ms: 1.08x slower                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 37.8 ms: 1.09x slower                                                      |
| xml_etree_process       | 37.1 ms                                                     | 40.3 ms: 1.09x slower                                                      |
| thrift                  | 491 us                                                      | 535 us: 1.09x slower                                                       |
| html5lib                | 37.5 ms                                                     | 41.5 ms: 1.11x slower                                                      |
| fannkuch                | 252 ms                                                      | 279 ms: 1.11x slower                                                       |
| python_startup          | 18.7 ms                                                     | 20.7 ms: 1.11x slower                                                      |
| chameleon               | 5.11 ms                                                     | 5.68 ms: 1.11x slower                                                      |
| go                      | 97.3 ms                                                     | 108 ms: 1.11x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.66 ms: 1.11x slower                                                      |
| pprint_safe_repr        | 512 ms                                                      | 570 ms: 1.11x slower                                                       |
| dask                    | 264 ms                                                      | 295 ms: 1.11x slower                                                       |
| regex_dna               | 115 ms                                                      | 129 ms: 1.11x slower                                                       |
| pprint_pformat          | 1.04 sec                                                    | 1.16 sec: 1.12x slower                                                     |
| async_generators        | 178 ms                                                      | 198 ms: 1.12x slower                                                       |
| mako                    | 7.26 ms                                                     | 8.12 ms: 1.12x slower                                                      |
| json_loads              | 12.9 us                                                     | 14.4 us: 1.12x slower                                                      |
| pycparser               | 691 ms                                                      | 777 ms: 1.12x slower                                                       |
| unpickle_pure_python    | 152 us                                                      | 172 us: 1.13x slower                                                       |
| richards                | 30.6 ms                                                     | 34.7 ms: 1.13x slower                                                      |
| hexiom                  | 4.55 ms                                                     | 5.17 ms: 1.13x slower                                                      |
| deepcopy_memo           | 25.2 us                                                     | 28.6 us: 1.13x slower                                                      |
| create_gc_cycles        | 693 us                                                      | 807 us: 1.17x slower                                                       |
| chaos                   | 47.1 ms                                                     | 55.0 ms: 1.17x slower                                                      |
| scimark_monte_carlo     | 44.6 ms                                                     | 52.6 ms: 1.18x slower                                                      |
| logging_silent          | 69.8 ns                                                     | 83.4 ns: 1.19x slower                                                      |
| deltablue               | 2.61 ms                                                     | 3.12 ms: 1.19x slower                                                      |
| pyflate                 | 304 ms                                                      | 365 ms: 1.20x slower                                                       |
| pickle_pure_python      | 200 us                                                      | 240 us: 1.20x slower                                                       |
| comprehensions          | 15.9 us                                                     | 19.1 us: 1.20x slower                                                      |
| scimark_fft             | 178 ms                                                      | 216 ms: 1.21x slower                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 57.7 ms: 1.21x slower                                                      |
| coroutines              | 14.6 ms                                                     | 17.9 ms: 1.22x slower                                                      |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 3.18 ms: 1.24x slower                                                      |
| nbody                   | 70.0 ms                                                     | 86.8 ms: 1.24x slower                                                      |
| spectral_norm           | 67.9 ms                                                     | 84.7 ms: 1.25x slower                                                      |
| scimark_lu              | 63.5 ms                                                     | 83.6 ms: 1.32x slower                                                      |
| sqlglot_transpile       | 1.16 ms                                                     | 1.53 ms: 1.32x slower                                                      |
| sqlglot_parse           | 952 us                                                      | 1.32 ms: 1.38x slower                                                      |
| scimark_sor             | 75.6 ms                                                     | 105 ms: 1.39x slower                                                       |
| coverage                | 55.9 ms                                                     | 261 ms: 4.68x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.09x slower                                                               |

Benchmark hidden because not significant (5): pickle, async_tree_io, flaskblogging, sympy_sum, genshi_xml
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, mypy2, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x
