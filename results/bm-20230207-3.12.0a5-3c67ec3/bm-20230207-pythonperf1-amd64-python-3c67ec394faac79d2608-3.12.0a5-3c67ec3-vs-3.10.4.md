
# Results vs. 3.10.4

- fork: python
- ref: 3c67ec394faac79d2608
- machine: windows-amd64
- commit hash: 3c67ec3
- commit date: 2023-02-07
- overall geometric mean: 1.23x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf1-amd64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 192 ms: 1.23x faster                                                       |
| chameleon      | 5.92 ms                                                     | 4.41 ms: 1.34x faster                                                      |
| docutils       | 1.89 sec                                                    | 1.50 sec: 1.26x faster                                                     |
| html5lib       | 46.5 ms                                                     | 34.1 ms: 1.36x faster                                                      |
| tornado_http   | 109 ms                                                      | 90.5 ms: 1.21x faster                                                      |
| Geometric mean | (ref)                                                       | 1.28x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf1-amd64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 47.3 ms: 1.27x faster                                                      |
| nbody          | 69.3 ms                                                     | 59.1 ms: 1.17x faster                                                      |
| pidigits       | 145 ms                                                      | 146 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf1-amd64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 78.8 ms: 1.31x faster                                                      |
| regex_v8       | 15.0 ms                                                     | 13.7 ms: 1.10x faster                                                      |
| regex_dna      | 132 ms                                                      | 121 ms: 1.09x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.68 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf1-amd64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.38 ms: 1.58x faster                                                      |
| pickle_pure_python   | 257 us                                                      | 166 us: 1.55x faster                                                       |
| unpickle_pure_python | 171 us                                                      | 120 us: 1.43x faster                                                       |
| xml_etree_process    | 43.4 ms                                                     | 33.5 ms: 1.30x faster                                                      |
| xml_etree_parse      | 102 ms                                                      | 88.5 ms: 1.15x faster                                                      |
| xml_etree_generate   | 54.5 ms                                                     | 49.5 ms: 1.10x faster                                                      |
| unpickle_list        | 2.81 us                                                     | 2.65 us: 1.06x faster                                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 62.3 ms: 1.02x faster                                                      |
| pickle               | 6.80 us                                                     | 6.77 us: 1.01x faster                                                      |
| unpickle             | 9.17 us                                                     | 9.39 us: 1.02x slower                                                      |
| pickle_list          | 2.59 us                                                     | 2.70 us: 1.04x slower                                                      |
| pickle_dict          | 16.9 us                                                     | 18.5 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf1-amd64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf1-amd64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.15 ms: 1.43x faster                                                      |
| django_template | 28.2 ms                                                     | 20.2 ms: 1.40x faster                                                      |
| genshi_text     | 19.0 ms                                                     | 14.2 ms: 1.34x faster                                                      |
| genshi_xml      | 40.5 ms                                                     | 32.6 ms: 1.24x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.35x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf1-amd64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 1.96 ms: 2.13x faster                                                      |
| go                      | 136 ms                                                      | 78.8 ms: 1.73x faster                                                      |
| richards                | 41.2 ms                                                     | 23.9 ms: 1.72x faster                                                      |
| mypy2                   | 352 ms                                                      | 208 ms: 1.69x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 58.1 ns: 1.66x faster                                                      |
| raytrace                | 271 ms                                                      | 170 ms: 1.59x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.38 ms: 1.58x faster                                                      |
| scimark_sor             | 105 ms                                                      | 67.0 ms: 1.57x faster                                                      |
| pickle_pure_python      | 257 us                                                      | 166 us: 1.55x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 466 ms: 1.53x faster                                                       |
| chaos                   | 58.9 ms                                                     | 39.6 ms: 1.49x faster                                                      |
| hexiom                  | 5.52 ms                                                     | 3.73 ms: 1.48x faster                                                      |
| unpack_sequence         | 37.8 ns                                                     | 25.6 ns: 1.48x faster                                                      |
| scimark_monte_carlo     | 55.9 ms                                                     | 37.9 ms: 1.47x faster                                                      |
| scimark_lu              | 85.4 ms                                                     | 58.7 ms: 1.46x faster                                                      |
| pyflate                 | 387 ms                                                      | 267 ms: 1.45x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 851 us: 1.43x faster                                                       |
| mako                    | 8.80 ms                                                     | 6.15 ms: 1.43x faster                                                      |
| unpickle_pure_python    | 171 us                                                      | 120 us: 1.43x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 748 ms: 1.42x faster                                                       |
| crypto_pyaes            | 62.3 ms                                                     | 44.0 ms: 1.42x faster                                                      |
| django_template         | 28.2 ms                                                     | 20.2 ms: 1.40x faster                                                      |
| async_tree_memoization  | 497 ms                                                      | 356 ms: 1.40x faster                                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.05 ms: 1.39x faster                                                      |
| async_tree_none         | 420 ms                                                      | 302 ms: 1.39x faster                                                       |
| pycparser               | 868 ms                                                      | 633 ms: 1.37x faster                                                       |
| comprehensions          | 16.0 us                                                     | 11.7 us: 1.37x faster                                                      |
| html5lib                | 46.5 ms                                                     | 34.1 ms: 1.36x faster                                                      |
| thrift                  | 615 us                                                      | 452 us: 1.36x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 21.1 us: 1.35x faster                                                      |
| chameleon               | 5.92 ms                                                     | 4.41 ms: 1.34x faster                                                      |
| async_generators        | 224 ms                                                      | 167 ms: 1.34x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 14.2 ms: 1.34x faster                                                      |
| pprint_pformat          | 1.21 sec                                                    | 907 ms: 1.33x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 445 ms: 1.32x faster                                                       |
| regex_compile           | 103 ms                                                      | 78.8 ms: 1.31x faster                                                      |
| xml_etree_process       | 43.4 ms                                                     | 33.5 ms: 1.30x faster                                                      |
| float                   | 60.2 ms                                                     | 47.3 ms: 1.27x faster                                                      |
| async_tree_cpu_io_mixed | 609 ms                                                      | 480 ms: 1.27x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 61.5 ms: 1.27x faster                                                      |
| docutils                | 1.89 sec                                                    | 1.50 sec: 1.26x faster                                                     |
| genshi_xml              | 40.5 ms                                                     | 32.6 ms: 1.24x faster                                                      |
| 2to3                    | 237 ms                                                      | 192 ms: 1.23x faster                                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 31.6 ms: 1.23x faster                                                      |
| nqueens                 | 67.0 ms                                                     | 54.6 ms: 1.23x faster                                                      |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.18 ms: 1.22x faster                                                      |
| fannkuch                | 258 ms                                                      | 213 ms: 1.21x faster                                                       |
| deepcopy                | 255 us                                                      | 211 us: 1.21x faster                                                       |
| tornado_http            | 109 ms                                                      | 90.5 ms: 1.21x faster                                                      |
| sympy_integrate         | 14.8 ms                                                     | 12.4 ms: 1.20x faster                                                      |
| sqlglot_normalize       | 202 ms                                                      | 171 ms: 1.19x faster                                                       |
| nbody                   | 69.3 ms                                                     | 59.1 ms: 1.17x faster                                                      |
| sympy_expand            | 315 ms                                                      | 269 ms: 1.17x faster                                                       |
| scimark_fft             | 193 ms                                                      | 166 ms: 1.16x faster                                                       |
| sympy_sum               | 104 ms                                                      | 89.5 ms: 1.16x faster                                                      |
| mdp                     | 1.71 sec                                                    | 1.48 sec: 1.16x faster                                                     |
| create_gc_cycles        | 782 us                                                      | 676 us: 1.16x faster                                                       |
| sympy_str               | 188 ms                                                      | 164 ms: 1.15x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 88.5 ms: 1.15x faster                                                      |
| bench_thread_pool       | 946 us                                                      | 823 us: 1.15x faster                                                       |
| deepcopy_reduce         | 2.16 us                                                     | 1.88 us: 1.15x faster                                                      |
| dulwich_log             | 47.6 ms                                                     | 41.9 ms: 1.14x faster                                                      |
| xml_etree_generate      | 54.5 ms                                                     | 49.5 ms: 1.10x faster                                                      |
| regex_v8                | 15.0 ms                                                     | 13.7 ms: 1.10x faster                                                      |
| python_startup          | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                      |
| regex_dna               | 132 ms                                                      | 121 ms: 1.09x faster                                                       |
| json                    | 3.05 ms                                                     | 2.81 ms: 1.08x faster                                                      |
| coroutines              | 15.9 ms                                                     | 14.8 ms: 1.08x faster                                                      |
| logging_format          | 6.66 us                                                     | 6.28 us: 1.06x faster                                                      |
| unpickle_list           | 2.81 us                                                     | 2.65 us: 1.06x faster                                                      |
| meteor_contest          | 72.5 ms                                                     | 69.1 ms: 1.05x faster                                                      |
| pathlib                 | 77.4 ms                                                     | 73.7 ms: 1.05x faster                                                      |
| logging_simple          | 6.20 us                                                     | 6.01 us: 1.03x faster                                                      |
| xml_etree_iterparse     | 63.5 ms                                                     | 62.3 ms: 1.02x faster                                                      |
| telco                   | 3.78 ms                                                     | 3.72 ms: 1.02x faster                                                      |
| sqlite_synth            | 1.84 us                                                     | 1.82 us: 1.01x faster                                                      |
| pickle                  | 6.80 us                                                     | 6.77 us: 1.01x faster                                                      |
| pidigits                | 145 ms                                                      | 146 ms: 1.01x slower                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.68 ms: 1.01x slower                                                      |
| bench_mp_pool           | 60.7 ms                                                     | 61.7 ms: 1.02x slower                                                      |
| unpickle                | 9.17 us                                                     | 9.39 us: 1.02x slower                                                      |
| pickle_list             | 2.59 us                                                     | 2.70 us: 1.04x slower                                                      |
| generators              | 31.6 ms                                                     | 33.0 ms: 1.05x slower                                                      |
| gc_traversal            | 1.34 ms                                                     | 1.45 ms: 1.08x slower                                                      |
| pickle_dict             | 16.9 us                                                     | 18.5 us: 1.09x slower                                                      |
| dask                    | 305 ms                                                      | 349 ms: 1.15x slower                                                       |
| coverage                | 40.0 ms                                                     | 51.8 ms: 1.30x slower                                                      |
| Geometric mean          | (ref)                                                       | 1.23x faster                                                               |

Benchmark hidden because not significant (2): python_startup_no_site, json_loads
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x
