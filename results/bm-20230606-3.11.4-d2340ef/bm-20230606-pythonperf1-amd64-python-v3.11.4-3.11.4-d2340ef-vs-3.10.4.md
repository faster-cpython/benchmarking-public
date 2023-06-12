
# Results vs. 3.10.4

- fork: python
- ref: v3.11.4
- machine: windows-amd64
- commit hash: d2340ef
- commit date: 2023-06-06
- overall geometric mean: 1.08x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf1-amd64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 221 ms: 1.07x faster                                        |
| chameleon      | 5.92 ms                                                     | 5.44 ms: 1.09x faster                                       |
| docutils       | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                      |
| html5lib       | 46.5 ms                                                     | 39.4 ms: 1.18x faster                                       |
| tornado_http   | 109 ms                                                      | 103 ms: 1.05x faster                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf1-amd64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 56.7 ms: 1.06x faster                                       |
| nbody          | 69.3 ms                                                     | 70.4 ms: 1.02x slower                                       |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                       | 1.00x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf1-amd64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 92.8 ms: 1.11x faster                                       |
| regex_dna      | 132 ms                                                      | 120 ms: 1.10x faster                                        |
| regex_effbot   | 1.66 ms                                                     | 1.52 ms: 1.10x faster                                       |
| regex_v8       | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf1-amd64-python-v3.11.4-3.11.4-d2340ef |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle_pure_python   | 257 us                                                      | 201 us: 1.28x faster                                        |
| xml_etree_process    | 43.4 ms                                                     | 37.9 ms: 1.15x faster                                       |
| tomli_loads          | 1.62 sec                                                    | 1.43 sec: 1.13x faster                                      |
| unpickle             | 9.17 us                                                     | 8.15 us: 1.13x faster                                       |
| unpickle_pure_python | 171 us                                                      | 153 us: 1.12x faster                                        |
| json_dumps           | 8.50 ms                                                     | 7.92 ms: 1.07x faster                                       |
| json_loads           | 14.2 us                                                     | 13.3 us: 1.07x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 96.4 ms: 1.06x faster                                       |
| unpickle_list        | 2.81 us                                                     | 2.73 us: 1.03x faster                                       |
| xml_etree_generate   | 54.5 ms                                                     | 53.8 ms: 1.01x faster                                       |
| pickle               | 6.80 us                                                     | 6.74 us: 1.01x faster                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 64.8 ms: 1.02x slower                                       |
| pickle_list          | 2.59 us                                                     | 2.78 us: 1.07x slower                                       |
| pickle_dict          | 16.9 us                                                     | 18.8 us: 1.11x slower                                       |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf1-amd64-python-v3.11.4-3.11.4-d2340ef |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 20.6 ms: 1.03x slower                                       |
| python_startup_no_site | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                       |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf1-amd64-python-v3.11.4-3.11.4-d2340ef |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 28.2 ms                                                     | 24.5 ms: 1.15x faster                                       |
| mako            | 8.80 ms                                                     | 7.67 ms: 1.15x faster                                       |
| genshi_text     | 19.0 ms                                                     | 17.8 ms: 1.07x faster                                       |
| genshi_xml      | 40.5 ms                                                     | 38.6 ms: 1.05x faster                                       |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf1-amd64-python-v3.11.4-3.11.4-d2340ef |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.71 ms: 1.54x faster                                       |
| scimark_sor             | 105 ms                                                      | 76.9 ms: 1.36x faster                                       |
| go                      | 136 ms                                                      | 100 ms: 1.36x faster                                        |
| scimark_lu              | 85.4 ms                                                     | 63.4 ms: 1.35x faster                                       |
| richards_super          | 51.7 ms                                                     | 38.6 ms: 1.34x faster                                       |
| logging_silent          | 96.4 ns                                                     | 72.1 ns: 1.34x faster                                       |
| richards                | 41.2 ms                                                     | 31.0 ms: 1.33x faster                                       |
| async_tree_io           | 1.07 sec                                                    | 813 ms: 1.31x faster                                        |
| raytrace                | 271 ms                                                      | 208 ms: 1.31x faster                                        |
| sqlglot_parse           | 1.22 ms                                                     | 936 us: 1.30x faster                                        |
| pickle_pure_python      | 257 us                                                      | 201 us: 1.28x faster                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 1.15 ms: 1.28x faster                                       |
| async_tree_memoization  | 497 ms                                                      | 392 ms: 1.27x faster                                        |
| thrift                  | 615 us                                                      | 486 us: 1.27x faster                                        |
| async_tree_none         | 420 ms                                                      | 334 ms: 1.26x faster                                        |
| crypto_pyaes            | 62.3 ms                                                     | 49.7 ms: 1.26x faster                                       |
| pyflate                 | 387 ms                                                      | 310 ms: 1.25x faster                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 45.1 ms: 1.24x faster                                       |
| hexiom                  | 5.52 ms                                                     | 4.55 ms: 1.21x faster                                       |
| async_generators        | 224 ms                                                      | 184 ms: 1.21x faster                                        |
| mypy2                   | 352 ms                                                      | 290 ms: 1.21x faster                                        |
| chaos                   | 58.9 ms                                                     | 48.8 ms: 1.21x faster                                       |
| pycparser               | 868 ms                                                      | 726 ms: 1.20x faster                                        |
| html5lib                | 46.5 ms                                                     | 39.4 ms: 1.18x faster                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 522 ms: 1.17x faster                                        |
| django_template         | 28.2 ms                                                     | 24.5 ms: 1.15x faster                                       |
| sqlalchemy_declarative  | 95.4 ms                                                     | 82.7 ms: 1.15x faster                                       |
| pprint_safe_repr        | 589 ms                                                      | 513 ms: 1.15x faster                                        |
| mako                    | 8.80 ms                                                     | 7.67 ms: 1.15x faster                                       |
| pprint_pformat          | 1.21 sec                                                    | 1.05 sec: 1.15x faster                                      |
| xml_etree_process       | 43.4 ms                                                     | 37.9 ms: 1.15x faster                                       |
| docutils                | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                      |
| tomli_loads             | 1.62 sec                                                    | 1.43 sec: 1.13x faster                                      |
| unpickle                | 9.17 us                                                     | 8.15 us: 1.13x faster                                       |
| unpickle_pure_python    | 171 us                                                      | 153 us: 1.12x faster                                        |
| deepcopy_memo           | 28.5 us                                                     | 25.6 us: 1.12x faster                                       |
| regex_compile           | 103 ms                                                      | 92.8 ms: 1.11x faster                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 35.2 ms: 1.11x faster                                       |
| regex_dna               | 132 ms                                                      | 120 ms: 1.10x faster                                        |
| regex_effbot            | 1.66 ms                                                     | 1.52 ms: 1.10x faster                                       |
| chameleon               | 5.92 ms                                                     | 5.44 ms: 1.09x faster                                       |
| regex_v8                | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                       |
| aiohttp                 | 1.01 ms                                                     | 936 us: 1.08x faster                                        |
| coroutines              | 15.9 ms                                                     | 14.8 ms: 1.07x faster                                       |
| json_dumps              | 8.50 ms                                                     | 7.92 ms: 1.07x faster                                       |
| genshi_text             | 19.0 ms                                                     | 17.8 ms: 1.07x faster                                       |
| 2to3                    | 237 ms                                                      | 221 ms: 1.07x faster                                        |
| json_loads              | 14.2 us                                                     | 13.3 us: 1.07x faster                                       |
| sympy_integrate         | 14.8 ms                                                     | 13.9 ms: 1.06x faster                                       |
| dask                    | 305 ms                                                      | 287 ms: 1.06x faster                                        |
| float                   | 60.2 ms                                                     | 56.7 ms: 1.06x faster                                       |
| xml_etree_parse         | 102 ms                                                      | 96.4 ms: 1.06x faster                                       |
| create_gc_cycles        | 782 us                                                      | 740 us: 1.06x faster                                        |
| tornado_http            | 109 ms                                                      | 103 ms: 1.05x faster                                        |
| sympy_expand            | 315 ms                                                      | 299 ms: 1.05x faster                                        |
| scimark_fft             | 193 ms                                                      | 184 ms: 1.05x faster                                        |
| sqlalchemy_imperative   | 11.0 ms                                                     | 10.4 ms: 1.05x faster                                       |
| genshi_xml              | 40.5 ms                                                     | 38.6 ms: 1.05x faster                                       |
| sqlglot_normalize       | 202 ms                                                      | 193 ms: 1.05x faster                                        |
| pylint                  | 347 ms                                                      | 331 ms: 1.05x faster                                        |
| sqlite_synth            | 1.84 us                                                     | 1.76 us: 1.05x faster                                       |
| spectral_norm           | 78.0 ms                                                     | 74.7 ms: 1.04x faster                                       |
| deepcopy                | 255 us                                                      | 246 us: 1.04x faster                                        |
| unpickle_list           | 2.81 us                                                     | 2.73 us: 1.03x faster                                       |
| deepcopy_reduce         | 2.16 us                                                     | 2.09 us: 1.03x faster                                       |
| nqueens                 | 67.0 ms                                                     | 65.1 ms: 1.03x faster                                       |
| dulwich_log             | 47.6 ms                                                     | 46.4 ms: 1.03x faster                                       |
| comprehensions          | 16.0 us                                                     | 15.6 us: 1.02x faster                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.60 ms: 1.02x faster                                       |
| sympy_sum               | 104 ms                                                      | 103 ms: 1.01x faster                                        |
| xml_etree_generate      | 54.5 ms                                                     | 53.8 ms: 1.01x faster                                       |
| pickle                  | 6.80 us                                                     | 6.74 us: 1.01x faster                                       |
| sympy_str               | 188 ms                                                      | 187 ms: 1.01x faster                                        |
| nbody                   | 69.3 ms                                                     | 70.4 ms: 1.02x slower                                       |
| xml_etree_iterparse     | 63.5 ms                                                     | 64.8 ms: 1.02x slower                                       |
| fannkuch                | 258 ms                                                      | 263 ms: 1.02x slower                                        |
| mdp                     | 1.71 sec                                                    | 1.76 sec: 1.03x slower                                      |
| python_startup          | 20.0 ms                                                     | 20.6 ms: 1.03x slower                                       |
| pidigits                | 145 ms                                                      | 151 ms: 1.04x slower                                        |
| telco                   | 3.78 ms                                                     | 4.00 ms: 1.06x slower                                       |
| meteor_contest          | 72.5 ms                                                     | 77.4 ms: 1.07x slower                                       |
| pickle_list             | 2.59 us                                                     | 2.78 us: 1.07x slower                                       |
| logging_simple          | 6.20 us                                                     | 6.71 us: 1.08x slower                                       |
| bench_mp_pool           | 60.7 ms                                                     | 66.1 ms: 1.09x slower                                       |
| logging_format          | 6.66 us                                                     | 7.26 us: 1.09x slower                                       |
| generators              | 31.6 ms                                                     | 34.5 ms: 1.09x slower                                       |
| pickle_dict             | 16.9 us                                                     | 18.8 us: 1.11x slower                                       |
| gc_traversal            | 1.34 ms                                                     | 1.52 ms: 1.13x slower                                       |
| python_startup_no_site  | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                       |
| json                    | 3.05 ms                                                     | 3.51 ms: 1.15x slower                                       |
| asyncio_tcp_ssl         | 2.03 sec                                                    | 2.41 sec: 1.19x slower                                      |
| unpack_sequence         | 37.8 ns                                                     | 48.1 ns: 1.27x slower                                       |
| asyncio_tcp             | 712 ms                                                      | 932 ms: 1.31x slower                                        |
| coverage                | 40.0 ms                                                     | 55.6 ms: 1.39x slower                                       |
| Geometric mean          | (ref)                                                       | 1.08x faster                                                |

Benchmark hidden because not significant (4): bench_thread_pool, flaskblogging, pathlib, typing_runtime_protocols
