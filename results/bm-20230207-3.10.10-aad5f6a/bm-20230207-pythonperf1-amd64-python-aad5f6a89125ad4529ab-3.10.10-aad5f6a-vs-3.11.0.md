
# Results vs. 3.11.0

- fork: python
- ref: aad5f6a89125ad4529ab
- machine: windows-amd64
- commit hash: aad5f6a
- commit date: 2023-02-07
- overall geometric mean: 1.12x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf1-amd64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 231 ms: 1.11x slower                                                      |
| chameleon      | 5.11 ms                                                     | 5.49 ms: 1.07x slower                                                     |
| docutils       | 1.60 sec                                                    | 1.84 sec: 1.15x slower                                                    |
| html5lib       | 37.5 ms                                                     | 48.2 ms: 1.28x slower                                                     |
| tornado_http   | 91.8 ms                                                     | 109 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.16x slower                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf1-amd64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 71.9 ms: 1.03x slower                                                     |
| float          | 54.6 ms                                                     | 60.6 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                       | 1.04x slower                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf1-amd64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                     | 15.0 ms: 1.08x slower                                                     |
| regex_compile  | 90.6 ms                                                     | 103 ms: 1.14x slower                                                      |
| regex_dna      | 115 ms                                                      | 132 ms: 1.14x slower                                                      |
| regex_effbot   | 1.50 ms                                                     | 1.81 ms: 1.21x slower                                                     |
| Geometric mean | (ref)                                                       | 1.14x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf1-amd64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate   | 52.2 ms                                                     | 53.3 ms: 1.02x slower                                                     |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.4 ms: 1.03x slower                                                     |
| pickle_dict          | 18.5 us                                                     | 19.1 us: 1.03x slower                                                     |
| pickle               | 6.61 us                                                     | 7.00 us: 1.06x slower                                                     |
| unpickle_list        | 2.55 us                                                     | 2.73 us: 1.07x slower                                                     |
| pickle_list          | 2.68 us                                                     | 2.91 us: 1.09x slower                                                     |
| json_loads           | 12.9 us                                                     | 14.2 us: 1.10x slower                                                     |
| unpickle             | 8.09 us                                                     | 9.05 us: 1.12x slower                                                     |
| xml_etree_process    | 37.1 ms                                                     | 42.7 ms: 1.15x slower                                                     |
| json_dumps           | 7.56 ms                                                     | 8.93 ms: 1.18x slower                                                     |
| unpickle_pure_python | 152 us                                                      | 180 us: 1.19x slower                                                      |
| pickle_pure_python   | 200 us                                                      | 267 us: 1.34x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf1-amd64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.0 ms: 1.06x faster                                                     |
| python_startup         | 18.7 ms                                                     | 19.8 ms: 1.06x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf1-amd64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 37.3 ms                                                     | 39.0 ms: 1.05x slower                                                     |
| genshi_text     | 17.0 ms                                                     | 18.3 ms: 1.08x slower                                                     |
| django_template | 24.1 ms                                                     | 29.2 ms: 1.21x slower                                                     |
| mako            | 7.26 ms                                                     | 8.84 ms: 1.22x slower                                                     |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                              |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf1-amd64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coverage                | 55.9 ms                                                     | 40.0 ms: 1.40x faster                                                     |
| unpack_sequence         | 46.1 ns                                                     | 40.8 ns: 1.13x faster                                                     |
| json                    | 3.25 ms                                                     | 3.06 ms: 1.06x faster                                                     |
| python_startup_no_site  | 15.9 ms                                                     | 15.0 ms: 1.06x faster                                                     |
| gc_traversal            | 1.46 ms                                                     | 1.40 ms: 1.04x faster                                                     |
| bench_mp_pool           | 62.5 ms                                                     | 60.0 ms: 1.04x faster                                                     |
| generators              | 33.8 ms                                                     | 32.5 ms: 1.04x faster                                                     |
| logging_format          | 7.01 us                                                     | 6.81 us: 1.03x faster                                                     |
| meteor_contest          | 74.7 ms                                                     | 72.9 ms: 1.03x faster                                                     |
| logging_simple          | 6.61 us                                                     | 6.45 us: 1.03x faster                                                     |
| comprehensions          | 15.9 us                                                     | 15.7 us: 1.02x faster                                                     |
| telco                   | 3.90 ms                                                     | 3.88 ms: 1.01x faster                                                     |
| nqueens                 | 64.9 ms                                                     | 65.3 ms: 1.01x slower                                                     |
| xml_etree_generate      | 52.2 ms                                                     | 53.3 ms: 1.02x slower                                                     |
| mdp                     | 1.67 sec                                                    | 1.71 sec: 1.02x slower                                                    |
| nbody                   | 70.0 ms                                                     | 71.9 ms: 1.03x slower                                                     |
| fannkuch                | 252 ms                                                      | 259 ms: 1.03x slower                                                      |
| xml_etree_iterparse     | 62.6 ms                                                     | 64.4 ms: 1.03x slower                                                     |
| pickle_dict             | 18.5 us                                                     | 19.1 us: 1.03x slower                                                     |
| deepcopy_reduce         | 2.07 us                                                     | 2.14 us: 1.03x slower                                                     |
| pylint                  | 326 ms                                                      | 340 ms: 1.04x slower                                                      |
| genshi_xml              | 37.3 ms                                                     | 39.0 ms: 1.05x slower                                                     |
| sympy_str               | 182 ms                                                      | 191 ms: 1.05x slower                                                      |
| pathlib                 | 71.4 ms                                                     | 75.0 ms: 1.05x slower                                                     |
| deepcopy                | 246 us                                                      | 258 us: 1.05x slower                                                      |
| python_startup          | 18.7 ms                                                     | 19.8 ms: 1.06x slower                                                     |
| pickle                  | 6.61 us                                                     | 7.00 us: 1.06x slower                                                     |
| sympy_integrate         | 13.8 ms                                                     | 14.6 ms: 1.06x slower                                                     |
| sqlglot_normalize       | 190 ms                                                      | 202 ms: 1.06x slower                                                      |
| sympy_expand            | 295 ms                                                      | 314 ms: 1.06x slower                                                      |
| sympy_sum               | 99.9 ms                                                     | 106 ms: 1.06x slower                                                      |
| unpickle_list           | 2.55 us                                                     | 2.73 us: 1.07x slower                                                     |
| chameleon               | 5.11 ms                                                     | 5.49 ms: 1.07x slower                                                     |
| genshi_text             | 17.0 ms                                                     | 18.3 ms: 1.08x slower                                                     |
| regex_v8                | 13.8 ms                                                     | 15.0 ms: 1.08x slower                                                     |
| coroutines              | 14.6 ms                                                     | 15.9 ms: 1.09x slower                                                     |
| pickle_list             | 2.68 us                                                     | 2.91 us: 1.09x slower                                                     |
| scimark_fft             | 178 ms                                                      | 194 ms: 1.09x slower                                                      |
| aiohttp                 | 899 us                                                      | 980 us: 1.09x slower                                                      |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.82 ms: 1.10x slower                                                     |
| json_loads              | 12.9 us                                                     | 14.2 us: 1.10x slower                                                     |
| dulwich_log             | 44.5 ms                                                     | 49.0 ms: 1.10x slower                                                     |
| sqlglot_optimize        | 34.9 ms                                                     | 38.5 ms: 1.10x slower                                                     |
| sqlite_synth            | 1.68 us                                                     | 1.86 us: 1.10x slower                                                     |
| 2to3                    | 209 ms                                                      | 231 ms: 1.11x slower                                                      |
| bench_thread_pool       | 852 us                                                      | 944 us: 1.11x slower                                                      |
| float                   | 54.6 ms                                                     | 60.6 ms: 1.11x slower                                                     |
| unpickle                | 8.09 us                                                     | 9.05 us: 1.12x slower                                                     |
| create_gc_cycles        | 693 us                                                      | 776 us: 1.12x slower                                                      |
| pprint_safe_repr        | 512 ms                                                      | 576 ms: 1.13x slower                                                      |
| sqlalchemy_imperative   | 10.2 ms                                                     | 11.5 ms: 1.13x slower                                                     |
| pprint_pformat          | 1.04 sec                                                    | 1.18 sec: 1.14x slower                                                    |
| regex_compile           | 90.6 ms                                                     | 103 ms: 1.14x slower                                                      |
| regex_dna               | 115 ms                                                      | 132 ms: 1.14x slower                                                      |
| docutils                | 1.60 sec                                                    | 1.84 sec: 1.15x slower                                                    |
| xml_etree_process       | 37.1 ms                                                     | 42.7 ms: 1.15x slower                                                     |
| deepcopy_memo           | 25.2 us                                                     | 29.1 us: 1.15x slower                                                     |
| json_dumps              | 7.56 ms                                                     | 8.93 ms: 1.18x slower                                                     |
| hexiom                  | 4.55 ms                                                     | 5.38 ms: 1.18x slower                                                     |
| unpickle_pure_python    | 152 us                                                      | 180 us: 1.19x slower                                                      |
| dask                    | 264 ms                                                      | 314 ms: 1.19x slower                                                      |
| tornado_http            | 91.8 ms                                                     | 109 ms: 1.19x slower                                                      |
| sqlalchemy_declarative  | 81.5 ms                                                     | 97.2 ms: 1.19x slower                                                     |
| django_template         | 24.1 ms                                                     | 29.2 ms: 1.21x slower                                                     |
| regex_effbot            | 1.50 ms                                                     | 1.81 ms: 1.21x slower                                                     |
| spectral_norm           | 67.9 ms                                                     | 82.5 ms: 1.21x slower                                                     |
| mako                    | 7.26 ms                                                     | 8.84 ms: 1.22x slower                                                     |
| async_tree_cpu_io_mixed | 501 ms                                                      | 615 ms: 1.23x slower                                                      |
| thrift                  | 491 us                                                      | 605 us: 1.23x slower                                                      |
| chaos                   | 47.1 ms                                                     | 58.2 ms: 1.23x slower                                                     |
| scimark_monte_carlo     | 44.6 ms                                                     | 55.2 ms: 1.24x slower                                                     |
| pycparser               | 691 ms                                                      | 855 ms: 1.24x slower                                                      |
| sqlglot_transpile       | 1.16 ms                                                     | 1.45 ms: 1.25x slower                                                     |
| raytrace                | 211 ms                                                      | 266 ms: 1.26x slower                                                      |
| async_generators        | 178 ms                                                      | 227 ms: 1.28x slower                                                      |
| html5lib                | 37.5 ms                                                     | 48.2 ms: 1.28x slower                                                     |
| sqlglot_parse           | 952 us                                                      | 1.23 ms: 1.29x slower                                                     |
| pyflate                 | 304 ms                                                      | 393 ms: 1.29x slower                                                      |
| async_tree_none         | 320 ms                                                      | 417 ms: 1.30x slower                                                      |
| scimark_lu              | 63.5 ms                                                     | 83.2 ms: 1.31x slower                                                     |
| async_tree_memoization  | 371 ms                                                      | 490 ms: 1.32x slower                                                      |
| crypto_pyaes            | 47.6 ms                                                     | 63.1 ms: 1.33x slower                                                     |
| pickle_pure_python      | 200 us                                                      | 267 us: 1.34x slower                                                      |
| async_tree_io           | 779 ms                                                      | 1.05 sec: 1.34x slower                                                    |
| scimark_sor             | 75.6 ms                                                     | 104 ms: 1.38x slower                                                      |
| richards                | 30.6 ms                                                     | 42.3 ms: 1.38x slower                                                     |
| logging_silent          | 69.8 ns                                                     | 99.1 ns: 1.42x slower                                                     |
| go                      | 97.3 ms                                                     | 138 ms: 1.42x slower                                                      |
| mypy2                   | 229 ms                                                      | 338 ms: 1.48x slower                                                      |
| deltablue               | 2.61 ms                                                     | 4.16 ms: 1.60x slower                                                     |
| Geometric mean          | (ref)                                                       | 1.12x slower                                                              |

Benchmark hidden because not significant (4): asyncio_tcp, pidigits, flaskblogging, xml_etree_parse
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x
