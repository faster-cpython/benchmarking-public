
# Results vs. 3.10.4

- fork: python
- ref: b1b375e2670a58fc37cb
- machine: linux-x86_64
- commit hash: b1b375e
- commit date: 2023-02-19
- overall geometric mean: 1.27x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 279 ms: 1.26x faster                                                         |
| chameleon      | 9.72 ms                                                      | 7.14 ms: 1.36x faster                                                        |
| docutils       | 3.40 sec                                                     | 2.80 sec: 1.22x faster                                                       |
| html5lib       | 94.6 ms                                                      | 68.0 ms: 1.39x faster                                                        |
| tornado_http   | 152 ms                                                       | 117 ms: 1.30x faster                                                         |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 110 ms                                                       | 70.9 ms: 1.56x faster                                                        |
| nbody          | 137 ms                                                       | 90.4 ms: 1.52x faster                                                        |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 142 ms: 1.36x faster                                                         |
| regex_v8       | 26.6 ms                                                      | 22.9 ms: 1.16x faster                                                        |
| regex_dna      | 259 ms                                                       | 225 ms: 1.15x faster                                                         |
| regex_effbot   | 2.99 ms                                                      | 3.42 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 206 us: 1.56x faster                                                         |
| pickle_pure_python   | 457 us                                                       | 305 us: 1.50x faster                                                         |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                        |
| xml_etree_process    | 76.0 ms                                                      | 57.1 ms: 1.33x faster                                                        |
| json_loads           | 30.0 us                                                      | 23.9 us: 1.25x faster                                                        |
| xml_etree_parse      | 162 ms                                                       | 141 ms: 1.15x faster                                                         |
| xml_etree_generate   | 94.6 ms                                                      | 83.2 ms: 1.14x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.09x faster                                                         |
| pickle_list          | 4.11 us                                                      | 3.79 us: 1.08x faster                                                        |
| unpickle             | 14.2 us                                                      | 13.3 us: 1.07x faster                                                        |
| unpickle_list        | 4.49 us                                                      | 4.44 us: 1.01x faster                                                        |
| pickle               | 9.94 us                                                      | 10.3 us: 1.03x slower                                                        |
| pickle_dict          | 30.0 us                                                      | 32.3 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.2 ms: 1.02x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.28 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.92 ms: 1.48x faster                                                        |
| django_template | 51.5 ms                                                      | 38.3 ms: 1.34x faster                                                        |
| genshi_text     | 31.5 ms                                                      | 24.7 ms: 1.27x faster                                                        |
| genshi_xml      | 64.7 ms                                                      | 53.6 ms: 1.21x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.32 ms: 2.25x faster                                                        |
| asyncio_tcp             | 782 ms                                                       | 386 ms: 2.03x faster                                                         |
| logging_silent          | 166 ns                                                       | 92.7 ns: 1.79x faster                                                        |
| go                      | 259 ms                                                       | 150 ms: 1.72x faster                                                         |
| scimark_sor             | 177 ms                                                       | 105 ms: 1.68x faster                                                         |
| raytrace                | 488 ms                                                       | 293 ms: 1.67x faster                                                         |
| richards                | 74.1 ms                                                      | 44.8 ms: 1.65x faster                                                        |
| scimark_lu              | 164 ms                                                       | 99.6 ms: 1.64x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 66.8 ms: 1.64x faster                                                        |
| pyflate                 | 697 ms                                                       | 434 ms: 1.61x faster                                                         |
| float                   | 110 ms                                                       | 70.9 ms: 1.56x faster                                                        |
| unpickle_pure_python    | 321 us                                                       | 206 us: 1.56x faster                                                         |
| nbody                   | 137 ms                                                       | 90.4 ms: 1.52x faster                                                        |
| bench_mp_pool           | 7.18 ms                                                      | 4.77 ms: 1.51x faster                                                        |
| pickle_pure_python      | 457 us                                                       | 305 us: 1.50x faster                                                         |
| chaos                   | 107 ms                                                       | 71.8 ms: 1.49x faster                                                        |
| hexiom                  | 9.52 ms                                                      | 6.39 ms: 1.49x faster                                                        |
| mako                    | 14.7 ms                                                      | 9.92 ms: 1.48x faster                                                        |
| crypto_pyaes            | 118 ms                                                       | 80.4 ms: 1.47x faster                                                        |
| sqlglot_parse           | 2.26 ms                                                      | 1.55 ms: 1.46x faster                                                        |
| generators              | 58.0 ms                                                      | 39.9 ms: 1.45x faster                                                        |
| spectral_norm           | 136 ms                                                       | 94.6 ms: 1.44x faster                                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 1.92 ms: 1.41x faster                                                        |
| deepcopy_memo           | 48.9 us                                                      | 35.0 us: 1.40x faster                                                        |
| json_dumps              | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                        |
| pprint_pformat          | 2.15 sec                                                     | 1.55 sec: 1.39x faster                                                       |
| html5lib                | 94.6 ms                                                      | 68.0 ms: 1.39x faster                                                        |
| pprint_safe_repr        | 1.05 sec                                                     | 759 ms: 1.38x faster                                                         |
| pycparser               | 1.66 sec                                                     | 1.21 sec: 1.38x faster                                                       |
| async_tree_none         | 700 ms                                                       | 507 ms: 1.38x faster                                                         |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.37x faster                                                       |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 3.78 ms: 1.37x faster                                                        |
| chameleon               | 9.72 ms                                                      | 7.14 ms: 1.36x faster                                                        |
| regex_compile           | 194 ms                                                       | 142 ms: 1.36x faster                                                         |
| async_tree_memoization  | 824 ms                                                       | 613 ms: 1.34x faster                                                         |
| django_template         | 51.5 ms                                                      | 38.3 ms: 1.34x faster                                                        |
| unpack_sequence         | 59.5 ns                                                      | 44.4 ns: 1.34x faster                                                        |
| xml_etree_process       | 76.0 ms                                                      | 57.1 ms: 1.33x faster                                                        |
| tornado_http            | 152 ms                                                       | 117 ms: 1.30x faster                                                         |
| logging_simple          | 8.90 us                                                      | 6.94 us: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 952 ms                                                       | 744 ms: 1.28x faster                                                         |
| comprehensions          | 26.9 us                                                      | 21.1 us: 1.28x faster                                                        |
| genshi_text             | 31.5 ms                                                      | 24.7 ms: 1.27x faster                                                        |
| scimark_fft             | 359 ms                                                       | 282 ms: 1.27x faster                                                         |
| thrift                  | 1.16 ms                                                      | 915 us: 1.27x faster                                                         |
| coroutines              | 30.4 ms                                                      | 24.0 ms: 1.27x faster                                                        |
| mypy2                   | 466 ms                                                       | 368 ms: 1.27x faster                                                         |
| 2to3                    | 350 ms                                                       | 279 ms: 1.26x faster                                                         |
| json_loads              | 30.0 us                                                      | 23.9 us: 1.25x faster                                                        |
| dulwich_log             | 80.1 ms                                                      | 65.2 ms: 1.23x faster                                                        |
| logging_format          | 9.57 us                                                      | 7.82 us: 1.22x faster                                                        |
| sqlglot_optimize        | 70.3 ms                                                      | 57.6 ms: 1.22x faster                                                        |
| docutils                | 3.40 sec                                                     | 2.80 sec: 1.22x faster                                                       |
| genshi_xml              | 64.7 ms                                                      | 53.6 ms: 1.21x faster                                                        |
| deepcopy_reduce         | 4.03 us                                                      | 3.34 us: 1.21x faster                                                        |
| sqlglot_normalize       | 144 ms                                                       | 120 ms: 1.20x faster                                                         |
| json                    | 5.96 ms                                                      | 5.00 ms: 1.19x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 956 us: 1.19x faster                                                         |
| deepcopy                | 454 us                                                       | 384 us: 1.18x faster                                                         |
| fannkuch                | 496 ms                                                       | 426 ms: 1.16x faster                                                         |
| regex_v8                | 26.6 ms                                                      | 22.9 ms: 1.16x faster                                                        |
| nqueens                 | 112 ms                                                       | 96.9 ms: 1.16x faster                                                        |
| mdp                     | 3.03 sec                                                     | 2.62 sec: 1.16x faster                                                       |
| regex_dna               | 259 ms                                                       | 225 ms: 1.15x faster                                                         |
| xml_etree_parse         | 162 ms                                                       | 141 ms: 1.15x faster                                                         |
| sympy_integrate         | 28.1 ms                                                      | 24.5 ms: 1.15x faster                                                        |
| xml_etree_generate      | 94.6 ms                                                      | 83.2 ms: 1.14x faster                                                        |
| sympy_str               | 358 ms                                                       | 315 ms: 1.13x faster                                                         |
| sqlite_synth            | 2.97 us                                                      | 2.63 us: 1.13x faster                                                        |
| async_generators        | 422 ms                                                       | 375 ms: 1.13x faster                                                         |
| create_gc_cycles        | 1.82 ms                                                      | 1.62 ms: 1.12x faster                                                        |
| sympy_expand            | 599 ms                                                       | 535 ms: 1.12x faster                                                         |
| pathlib                 | 21.7 ms                                                      | 19.4 ms: 1.12x faster                                                        |
| sympy_sum               | 193 ms                                                       | 176 ms: 1.10x faster                                                         |
| xml_etree_iterparse     | 110 ms                                                       | 101 ms: 1.09x faster                                                         |
| pickle_list             | 4.11 us                                                      | 3.79 us: 1.08x faster                                                        |
| pidigits                | 271 ms                                                       | 252 ms: 1.07x faster                                                         |
| meteor_contest          | 137 ms                                                       | 128 ms: 1.07x faster                                                         |
| unpickle                | 14.2 us                                                      | 13.3 us: 1.07x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.73 ms: 1.06x faster                                                        |
| python_startup          | 11.5 ms                                                      | 11.2 ms: 1.02x faster                                                        |
| unpickle_list           | 4.49 us                                                      | 4.44 us: 1.01x faster                                                        |
| pickle                  | 9.94 us                                                      | 10.3 us: 1.03x slower                                                        |
| gc_traversal            | 3.45 ms                                                      | 3.57 ms: 1.04x slower                                                        |
| pickle_dict             | 30.0 us                                                      | 32.3 us: 1.08x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.28 ms: 1.13x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.42 ms: 1.14x slower                                                        |
| dask                    | 463 ms                                                       | 558 ms: 1.21x slower                                                         |
| coverage                | 64.0 ms                                                      | 85.0 ms: 1.33x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                                 |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x
