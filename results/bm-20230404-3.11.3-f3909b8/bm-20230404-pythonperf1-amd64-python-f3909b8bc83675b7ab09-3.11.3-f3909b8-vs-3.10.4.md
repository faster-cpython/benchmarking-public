
# Results vs. 3.10.4

- fork: python
- ref: f3909b8bc83675b7ab09
- machine: windows-amd64
- commit hash: f3909b8
- commit date: 2023-04-04
- overall geometric mean: 1.12x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf1-amd64-python-f3909b8bc83675b7ab09-3.11.3-f3909b8 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 206 ms: 1.15x faster                                                     |
| chameleon      | 5.92 ms                                                     | 5.27 ms: 1.12x faster                                                    |
| docutils       | 1.89 sec                                                    | 1.58 sec: 1.20x faster                                                   |
| html5lib       | 46.5 ms                                                     | 39.8 ms: 1.17x faster                                                    |
| tornado_http   | 109 ms                                                      | 90.1 ms: 1.21x faster                                                    |
| Geometric mean | (ref)                                                       | 1.17x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf1-amd64-python-f3909b8bc83675b7ab09-3.11.3-f3909b8 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 52.6 ms: 1.15x faster                                                    |
| nbody          | 69.3 ms                                                     | 69.8 ms: 1.01x slower                                                    |
| pidigits       | 145 ms                                                      | 147 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                       | 1.04x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf1-amd64-python-f3909b8bc83675b7ab09-3.11.3-f3909b8 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 89.7 ms: 1.15x faster                                                    |
| regex_dna      | 132 ms                                                      | 120 ms: 1.10x faster                                                     |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                    |
| regex_v8       | 15.0 ms                                                     | 14.3 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                       | 1.09x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf1-amd64-python-f3909b8bc83675b7ab09-3.11.3-f3909b8 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 257 us                                                      | 198 us: 1.30x faster                                                     |
| xml_etree_process    | 43.4 ms                                                     | 36.3 ms: 1.20x faster                                                    |
| unpickle             | 9.17 us                                                     | 7.97 us: 1.15x faster                                                    |
| unpickle_pure_python | 171 us                                                      | 150 us: 1.14x faster                                                     |
| json_dumps           | 8.50 ms                                                     | 7.60 ms: 1.12x faster                                                    |
| xml_etree_parse      | 102 ms                                                      | 91.3 ms: 1.12x faster                                                    |
| json_loads           | 14.2 us                                                     | 13.0 us: 1.09x faster                                                    |
| xml_etree_generate   | 54.5 ms                                                     | 51.8 ms: 1.05x faster                                                    |
| unpickle_list        | 2.81 us                                                     | 2.68 us: 1.05x faster                                                    |
| xml_etree_iterparse  | 63.5 ms                                                     | 61.4 ms: 1.03x faster                                                    |
| pickle               | 6.80 us                                                     | 6.73 us: 1.01x faster                                                    |
| pickle_list          | 2.59 us                                                     | 2.78 us: 1.07x slower                                                    |
| pickle_dict          | 16.9 us                                                     | 18.6 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf1-amd64-python-f3909b8bc83675b7ab09-3.11.3-f3909b8 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 18.4 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                       | 1.05x faster                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf1-amd64-python-f3909b8bc83675b7ab09-3.11.3-f3909b8 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 7.22 ms: 1.22x faster                                                    |
| django_template | 28.2 ms                                                     | 23.8 ms: 1.18x faster                                                    |
| genshi_text     | 19.0 ms                                                     | 17.3 ms: 1.10x faster                                                    |
| genshi_xml      | 40.5 ms                                                     | 37.6 ms: 1.08x faster                                                    |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf1-amd64-python-f3909b8bc83675b7ab09-3.11.3-f3909b8 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.65 ms: 1.57x faster                                                    |
| async_tree_io           | 1.07 sec                                                    | 739 ms: 1.44x faster                                                     |
| scimark_sor             | 105 ms                                                      | 75.2 ms: 1.39x faster                                                    |
| logging_silent          | 96.4 ns                                                     | 70.1 ns: 1.38x faster                                                    |
| go                      | 136 ms                                                      | 99.2 ms: 1.37x faster                                                    |
| richards                | 41.2 ms                                                     | 30.4 ms: 1.35x faster                                                    |
| async_tree_memoization  | 497 ms                                                      | 368 ms: 1.35x faster                                                     |
| scimark_lu              | 85.4 ms                                                     | 63.3 ms: 1.35x faster                                                    |
| raytrace                | 271 ms                                                      | 203 ms: 1.34x faster                                                     |
| async_tree_none         | 420 ms                                                      | 314 ms: 1.34x faster                                                     |
| sqlglot_parse           | 1.22 ms                                                     | 931 us: 1.31x faster                                                     |
| pickle_pure_python      | 257 us                                                      | 198 us: 1.30x faster                                                     |
| crypto_pyaes            | 62.3 ms                                                     | 48.2 ms: 1.29x faster                                                    |
| sqlglot_transpile       | 1.46 ms                                                     | 1.13 ms: 1.29x faster                                                    |
| pyflate                 | 387 ms                                                      | 301 ms: 1.28x faster                                                     |
| thrift                  | 615 us                                                      | 482 us: 1.28x faster                                                     |
| async_generators        | 224 ms                                                      | 176 ms: 1.27x faster                                                     |
| mypy2                   | 352 ms                                                      | 280 ms: 1.26x faster                                                     |
| scimark_monte_carlo     | 55.9 ms                                                     | 45.1 ms: 1.24x faster                                                    |
| pycparser               | 868 ms                                                      | 703 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed | 609 ms                                                      | 500 ms: 1.22x faster                                                     |
| mako                    | 8.80 ms                                                     | 7.22 ms: 1.22x faster                                                    |
| tornado_http            | 109 ms                                                      | 90.1 ms: 1.21x faster                                                    |
| hexiom                  | 5.52 ms                                                     | 4.56 ms: 1.21x faster                                                    |
| chaos                   | 58.9 ms                                                     | 48.9 ms: 1.20x faster                                                    |
| xml_etree_process       | 43.4 ms                                                     | 36.3 ms: 1.20x faster                                                    |
| docutils                | 1.89 sec                                                    | 1.58 sec: 1.20x faster                                                   |
| django_template         | 28.2 ms                                                     | 23.8 ms: 1.18x faster                                                    |
| create_gc_cycles        | 782 us                                                      | 664 us: 1.18x faster                                                     |
| sqlalchemy_declarative  | 95.4 ms                                                     | 81.1 ms: 1.18x faster                                                    |
| aiohttp                 | 1.01 ms                                                     | 857 us: 1.18x faster                                                     |
| html5lib                | 46.5 ms                                                     | 39.8 ms: 1.17x faster                                                    |
| dask                    | 305 ms                                                      | 261 ms: 1.17x faster                                                     |
| spectral_norm           | 78.0 ms                                                     | 67.6 ms: 1.15x faster                                                    |
| regex_compile           | 103 ms                                                      | 89.7 ms: 1.15x faster                                                    |
| unpickle                | 9.17 us                                                     | 7.97 us: 1.15x faster                                                    |
| deepcopy_memo           | 28.5 us                                                     | 24.8 us: 1.15x faster                                                    |
| 2to3                    | 237 ms                                                      | 206 ms: 1.15x faster                                                     |
| float                   | 60.2 ms                                                     | 52.6 ms: 1.15x faster                                                    |
| unpickle_pure_python    | 171 us                                                      | 150 us: 1.14x faster                                                     |
| pprint_pformat          | 1.21 sec                                                    | 1.06 sec: 1.14x faster                                                   |
| chameleon               | 5.92 ms                                                     | 5.27 ms: 1.12x faster                                                    |
| sqlglot_optimize        | 39.0 ms                                                     | 34.7 ms: 1.12x faster                                                    |
| pprint_safe_repr        | 589 ms                                                      | 526 ms: 1.12x faster                                                     |
| dulwich_log             | 47.6 ms                                                     | 42.5 ms: 1.12x faster                                                    |
| json_dumps              | 8.50 ms                                                     | 7.60 ms: 1.12x faster                                                    |
| bench_thread_pool       | 946 us                                                      | 848 us: 1.12x faster                                                     |
| xml_etree_parse         | 102 ms                                                      | 91.3 ms: 1.12x faster                                                    |
| genshi_text             | 19.0 ms                                                     | 17.3 ms: 1.10x faster                                                    |
| regex_dna               | 132 ms                                                      | 120 ms: 1.10x faster                                                     |
| sqlalchemy_imperative   | 11.0 ms                                                     | 10.0 ms: 1.09x faster                                                    |
| json_loads              | 14.2 us                                                     | 13.0 us: 1.09x faster                                                    |
| sympy_integrate         | 14.8 ms                                                     | 13.6 ms: 1.09x faster                                                    |
| sympy_expand            | 315 ms                                                      | 290 ms: 1.09x faster                                                     |
| sqlite_synth            | 1.84 us                                                     | 1.69 us: 1.09x faster                                                    |
| python_startup          | 20.0 ms                                                     | 18.4 ms: 1.08x faster                                                    |
| pylint                  | 347 ms                                                      | 321 ms: 1.08x faster                                                     |
| genshi_xml              | 40.5 ms                                                     | 37.6 ms: 1.08x faster                                                    |
| regex_effbot            | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                    |
| sqlglot_normalize       | 202 ms                                                      | 191 ms: 1.06x faster                                                     |
| sympy_sum               | 104 ms                                                      | 98.4 ms: 1.06x faster                                                    |
| deepcopy_reduce         | 2.16 us                                                     | 2.04 us: 1.06x faster                                                    |
| pathlib                 | 77.4 ms                                                     | 73.2 ms: 1.06x faster                                                    |
| regex_v8                | 15.0 ms                                                     | 14.3 ms: 1.05x faster                                                    |
| xml_etree_generate      | 54.5 ms                                                     | 51.8 ms: 1.05x faster                                                    |
| coroutines              | 15.9 ms                                                     | 15.1 ms: 1.05x faster                                                    |
| deepcopy                | 255 us                                                      | 243 us: 1.05x faster                                                     |
| unpickle_list           | 2.81 us                                                     | 2.68 us: 1.05x faster                                                    |
| scimark_fft             | 193 ms                                                      | 185 ms: 1.05x faster                                                     |
| comprehensions          | 16.0 us                                                     | 15.4 us: 1.04x faster                                                    |
| sympy_str               | 188 ms                                                      | 182 ms: 1.04x faster                                                     |
| xml_etree_iterparse     | 63.5 ms                                                     | 61.4 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.58 ms: 1.03x faster                                                    |
| nqueens                 | 67.0 ms                                                     | 65.6 ms: 1.02x faster                                                    |
| pickle                  | 6.80 us                                                     | 6.73 us: 1.01x faster                                                    |
| flaskblogging           | 2.04 sec                                                    | 2.05 sec: 1.00x slower                                                   |
| nbody                   | 69.3 ms                                                     | 69.8 ms: 1.01x slower                                                    |
| pidigits                | 145 ms                                                      | 147 ms: 1.01x slower                                                     |
| mdp                     | 1.71 sec                                                    | 1.74 sec: 1.02x slower                                                   |
| bench_mp_pool           | 60.7 ms                                                     | 62.0 ms: 1.02x slower                                                    |
| meteor_contest          | 72.5 ms                                                     | 74.7 ms: 1.03x slower                                                    |
| logging_format          | 6.66 us                                                     | 6.99 us: 1.05x slower                                                    |
| gc_traversal            | 1.34 ms                                                     | 1.43 ms: 1.06x slower                                                    |
| telco                   | 3.78 ms                                                     | 4.02 ms: 1.06x slower                                                    |
| json                    | 3.05 ms                                                     | 3.25 ms: 1.07x slower                                                    |
| pickle_list             | 2.59 us                                                     | 2.78 us: 1.07x slower                                                    |
| generators              | 31.6 ms                                                     | 34.0 ms: 1.08x slower                                                    |
| logging_simple          | 6.20 us                                                     | 6.67 us: 1.08x slower                                                    |
| pickle_dict             | 16.9 us                                                     | 18.6 us: 1.10x slower                                                    |
| unpack_sequence         | 37.8 ns                                                     | 46.0 ns: 1.22x slower                                                    |
| coverage                | 40.0 ms                                                     | 53.2 ms: 1.33x slower                                                    |
| Geometric mean          | (ref)                                                       | 1.12x faster                                                             |

Benchmark hidden because not significant (3): python_startup_no_site, fannkuch, asyncio_tcp
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x
