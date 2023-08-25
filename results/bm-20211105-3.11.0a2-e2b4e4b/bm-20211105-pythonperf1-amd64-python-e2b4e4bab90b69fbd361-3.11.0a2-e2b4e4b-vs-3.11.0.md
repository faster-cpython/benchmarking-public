
# Results vs. 3.11.0

- fork: python
- ref: e2b4e4bab90b69fbd361
- machine: windows-amd64
- commit hash: e2b4e4b
- commit date: 2021-11-05
- overall geometric mean: 1.08x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 210 ms: 1.01x slower                                                       |
| chameleon      | 5.11 ms                                                     | 5.53 ms: 1.08x slower                                                      |
| docutils       | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                                     |
| html5lib       | 37.5 ms                                                     | 41.4 ms: 1.10x slower                                                      |
| tornado_http   | 91.8 ms                                                     | 98.3 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 148 ms: 1.00x faster                                                       |
| float          | 54.6 ms                                                     | 56.1 ms: 1.03x slower                                                      |
| nbody          | 70.0 ms                                                     | 90.3 ms: 1.29x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 115 ms                                                      | 131 ms: 1.14x slower                                                       |
| regex_v8       | 13.8 ms                                                     | 16.6 ms: 1.20x slower                                                      |
| regex_effbot   | 1.50 ms                                                     | 1.82 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                       | 1.13x slower                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_dict          | 18.5 us                                                     | 16.2 us: 1.14x faster                                                      |
| pickle_list          | 2.68 us                                                     | 2.49 us: 1.08x faster                                                      |
| unpickle             | 8.09 us                                                     | 7.81 us: 1.04x faster                                                      |
| xml_etree_parse      | 95.9 ms                                                     | 93.8 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 65.2 ms: 1.04x slower                                                      |
| xml_etree_generate   | 52.2 ms                                                     | 54.7 ms: 1.05x slower                                                      |
| json_dumps           | 7.56 ms                                                     | 7.94 ms: 1.05x slower                                                      |
| xml_etree_process    | 37.1 ms                                                     | 39.7 ms: 1.07x slower                                                      |
| unpickle_pure_python | 152 us                                                      | 168 us: 1.11x slower                                                       |
| pickle_pure_python   | 200 us                                                      | 228 us: 1.14x slower                                                       |
| json_loads           | 12.9 us                                                     | 14.9 us: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (2): unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.1 ms: 1.05x faster                                                      |
| python_startup         | 18.7 ms                                                     | 18.8 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 37.3 ms                                                     | 38.5 ms: 1.03x slower                                                      |
| genshi_text     | 17.0 ms                                                     | 17.5 ms: 1.03x slower                                                      |
| django_template | 24.1 ms                                                     | 26.0 ms: 1.08x slower                                                      |
| mako            | 7.26 ms                                                     | 8.07 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| logging_simple          | 6.61 us                                                     | 5.45 us: 1.21x faster                                                      |
| logging_format          | 7.01 us                                                     | 5.92 us: 1.18x faster                                                      |
| pickle_dict             | 18.5 us                                                     | 16.2 us: 1.14x faster                                                      |
| generators              | 33.8 ms                                                     | 31.0 ms: 1.09x faster                                                      |
| pickle_list             | 2.68 us                                                     | 2.49 us: 1.08x faster                                                      |
| json                    | 3.25 ms                                                     | 3.06 ms: 1.06x faster                                                      |
| gc_traversal            | 1.46 ms                                                     | 1.37 ms: 1.06x faster                                                      |
| python_startup_no_site  | 15.9 ms                                                     | 15.1 ms: 1.05x faster                                                      |
| async_tree_none         | 320 ms                                                      | 307 ms: 1.04x faster                                                       |
| unpickle                | 8.09 us                                                     | 7.81 us: 1.04x faster                                                      |
| mdp                     | 1.67 sec                                                    | 1.61 sec: 1.04x faster                                                     |
| xml_etree_parse         | 95.9 ms                                                     | 93.8 ms: 1.02x faster                                                      |
| bench_mp_pool           | 62.5 ms                                                     | 61.4 ms: 1.02x faster                                                      |
| dulwich_log             | 44.5 ms                                                     | 44.1 ms: 1.01x faster                                                      |
| pidigits                | 148 ms                                                      | 148 ms: 1.00x faster                                                       |
| 2to3                    | 209 ms                                                      | 210 ms: 1.01x slower                                                       |
| python_startup          | 18.7 ms                                                     | 18.8 ms: 1.01x slower                                                      |
| raytrace                | 211 ms                                                      | 214 ms: 1.01x slower                                                       |
| sympy_sum               | 99.9 ms                                                     | 102 ms: 1.02x slower                                                       |
| async_tree_io           | 779 ms                                                      | 793 ms: 1.02x slower                                                       |
| meteor_contest          | 74.7 ms                                                     | 76.2 ms: 1.02x slower                                                      |
| float                   | 54.6 ms                                                     | 56.1 ms: 1.03x slower                                                      |
| pathlib                 | 71.4 ms                                                     | 73.4 ms: 1.03x slower                                                      |
| genshi_xml              | 37.3 ms                                                     | 38.5 ms: 1.03x slower                                                      |
| sqlglot_normalize       | 190 ms                                                      | 196 ms: 1.03x slower                                                       |
| logging_silent          | 69.8 ns                                                     | 72.1 ns: 1.03x slower                                                      |
| genshi_text             | 17.0 ms                                                     | 17.5 ms: 1.03x slower                                                      |
| nqueens                 | 64.9 ms                                                     | 67.3 ms: 1.04x slower                                                      |
| sqlalchemy_imperative   | 10.2 ms                                                     | 10.6 ms: 1.04x slower                                                      |
| xml_etree_iterparse     | 62.6 ms                                                     | 65.2 ms: 1.04x slower                                                      |
| sympy_integrate         | 13.8 ms                                                     | 14.4 ms: 1.04x slower                                                      |
| docutils                | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                                     |
| xml_etree_generate      | 52.2 ms                                                     | 54.7 ms: 1.05x slower                                                      |
| sympy_str               | 182 ms                                                      | 191 ms: 1.05x slower                                                       |
| json_dumps              | 7.56 ms                                                     | 7.94 ms: 1.05x slower                                                      |
| sympy_expand            | 295 ms                                                      | 311 ms: 1.05x slower                                                       |
| async_tree_cpu_io_mixed | 501 ms                                                      | 530 ms: 1.06x slower                                                       |
| bench_thread_pool       | 852 us                                                      | 906 us: 1.06x slower                                                       |
| async_tree_memoization  | 371 ms                                                      | 395 ms: 1.07x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.80 us: 1.07x slower                                                      |
| pprint_safe_repr        | 512 ms                                                      | 547 ms: 1.07x slower                                                       |
| tornado_http            | 91.8 ms                                                     | 98.3 ms: 1.07x slower                                                      |
| xml_etree_process       | 37.1 ms                                                     | 39.7 ms: 1.07x slower                                                      |
| sqlglot_optimize        | 34.9 ms                                                     | 37.5 ms: 1.07x slower                                                      |
| thrift                  | 491 us                                                      | 528 us: 1.08x slower                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 2.23 us: 1.08x slower                                                      |
| async_generators        | 178 ms                                                      | 192 ms: 1.08x slower                                                       |
| django_template         | 24.1 ms                                                     | 26.0 ms: 1.08x slower                                                      |
| chameleon               | 5.11 ms                                                     | 5.53 ms: 1.08x slower                                                      |
| deepcopy                | 246 us                                                      | 266 us: 1.08x slower                                                       |
| pprint_pformat          | 1.04 sec                                                    | 1.13 sec: 1.08x slower                                                     |
| sqlalchemy_declarative  | 81.5 ms                                                     | 88.5 ms: 1.09x slower                                                      |
| fannkuch                | 252 ms                                                      | 275 ms: 1.09x slower                                                       |
| go                      | 97.3 ms                                                     | 106 ms: 1.09x slower                                                       |
| deltablue               | 2.61 ms                                                     | 2.86 ms: 1.09x slower                                                      |
| html5lib                | 37.5 ms                                                     | 41.4 ms: 1.10x slower                                                      |
| unpickle_pure_python    | 152 us                                                      | 168 us: 1.11x slower                                                       |
| hexiom                  | 4.55 ms                                                     | 5.06 ms: 1.11x slower                                                      |
| mako                    | 7.26 ms                                                     | 8.07 ms: 1.11x slower                                                      |
| richards                | 30.6 ms                                                     | 34.0 ms: 1.11x slower                                                      |
| pycparser               | 691 ms                                                      | 769 ms: 1.11x slower                                                       |
| dask                    | 264 ms                                                      | 295 ms: 1.11x slower                                                       |
| deepcopy_memo           | 25.2 us                                                     | 28.1 us: 1.12x slower                                                      |
| unpack_sequence         | 46.1 ns                                                     | 51.9 ns: 1.13x slower                                                      |
| regex_dna               | 115 ms                                                      | 131 ms: 1.14x slower                                                       |
| pickle_pure_python      | 200 us                                                      | 228 us: 1.14x slower                                                       |
| chaos                   | 47.1 ms                                                     | 53.9 ms: 1.14x slower                                                      |
| scimark_monte_carlo     | 44.6 ms                                                     | 51.7 ms: 1.16x slower                                                      |
| json_loads              | 12.9 us                                                     | 14.9 us: 1.16x slower                                                      |
| pyflate                 | 304 ms                                                      | 358 ms: 1.18x slower                                                       |
| scimark_fft             | 178 ms                                                      | 212 ms: 1.19x slower                                                       |
| comprehensions          | 15.9 us                                                     | 19.1 us: 1.20x slower                                                      |
| regex_v8                | 13.8 ms                                                     | 16.6 ms: 1.20x slower                                                      |
| regex_effbot            | 1.50 ms                                                     | 1.82 ms: 1.22x slower                                                      |
| spectral_norm           | 67.9 ms                                                     | 82.7 ms: 1.22x slower                                                      |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 3.18 ms: 1.24x slower                                                      |
| coroutines              | 14.6 ms                                                     | 18.1 ms: 1.24x slower                                                      |
| crypto_pyaes            | 47.6 ms                                                     | 58.9 ms: 1.24x slower                                                      |
| scimark_lu              | 63.5 ms                                                     | 81.5 ms: 1.28x slower                                                      |
| sqlglot_transpile       | 1.16 ms                                                     | 1.50 ms: 1.29x slower                                                      |
| nbody                   | 70.0 ms                                                     | 90.3 ms: 1.29x slower                                                      |
| scimark_sor             | 75.6 ms                                                     | 101 ms: 1.34x slower                                                       |
| sqlglot_parse           | 952 us                                                      | 1.29 ms: 1.36x slower                                                      |
| coverage                | 55.9 ms                                                     | 262 ms: 4.69x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (8): pylint, create_gc_cycles, asyncio_tcp, unpickle_list, regex_compile, pickle, telco, flaskblogging
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, mypy2, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x
