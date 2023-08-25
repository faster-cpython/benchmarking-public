
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 3eb12df
- commit date: 2023-02-11
- overall geometric mean: 1.25x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 181 ms: 1.12x faster                                   |
| chameleon      | 5.84 ms                                                | 4.34 ms: 1.35x faster                                  |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.22x faster                                 |
| html5lib       | 44.1 ms                                                | 35.0 ms: 1.26x faster                                  |
| tornado_http   | 91.9 ms                                                | 68.4 ms: 1.34x faster                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 63.1 ms: 1.49x faster                                  |
| float          | 72.3 ms                                                | 49.7 ms: 1.46x faster                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 71.0 ms: 1.36x faster                                  |
| regex_v8       | 17.5 ms                                                | 16.0 ms: 1.09x faster                                  |
| regex_dna      | 160 ms                                                 | 150 ms: 1.07x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.60 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 185 us: 1.53x faster                                   |
| unpickle_pure_python | 203 us                                                 | 137 us: 1.48x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.06 ms: 1.38x faster                                  |
| xml_etree_process    | 45.1 ms                                                | 35.2 ms: 1.28x faster                                  |
| xml_etree_parse      | 107 ms                                                 | 93.0 ms: 1.15x faster                                  |
| xml_etree_generate   | 54.3 ms                                                | 49.2 ms: 1.10x faster                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 67.1 ms: 1.08x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.03x faster                                  |
| unpickle_list        | 2.66 us                                                | 2.67 us: 1.00x slower                                  |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| unpickle             | 9.77 us                                                | 9.91 us: 1.01x slower                                  |
| pickle               | 7.36 us                                                | 7.57 us: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 9.36 ms: 1.35x faster                                  |
| python_startup_no_site | 9.73 ms                                                | 7.38 ms: 1.32x faster                                  |
| Geometric mean         | (ref)                                                  | 1.33x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.13 ms: 1.47x faster                                  |
| genshi_xml      | 37.6 ms                                                | 27.5 ms: 1.37x faster                                  |
| genshi_text     | 18.4 ms                                                | 13.8 ms: 1.33x faster                                  |
| django_template | 27.3 ms                                                | 20.8 ms: 1.32x faster                                  |
| Geometric mean  | (ref)                                                  | 1.37x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.47 ms: 2.08x faster                                  |
| logging_silent          | 119 ns                                                 | 64.1 ns: 1.86x faster                                  |
| richards                | 51.4 ms                                                | 29.5 ms: 1.74x faster                                  |
| asyncio_tcp             | 673 ms                                                 | 411 ms: 1.64x faster                                   |
| scimark_lu              | 110 ms                                                 | 70.5 ms: 1.56x faster                                  |
| async_tree_memoization  | 493 ms                                                 | 320 ms: 1.54x faster                                   |
| go                      | 165 ms                                                 | 107 ms: 1.54x faster                                   |
| pickle_pure_python      | 284 us                                                 | 185 us: 1.53x faster                                   |
| scimark_sor             | 127 ms                                                 | 83.4 ms: 1.52x faster                                  |
| raytrace                | 328 ms                                                 | 217 ms: 1.51x faster                                   |
| hexiom                  | 6.32 ms                                                | 4.21 ms: 1.50x faster                                  |
| nbody                   | 94.1 ms                                                | 63.1 ms: 1.49x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 137 us: 1.48x faster                                   |
| mako                    | 10.5 ms                                                | 7.13 ms: 1.47x faster                                  |
| chaos                   | 66.8 ms                                                | 45.5 ms: 1.47x faster                                  |
| crypto_pyaes            | 78.0 ms                                                | 53.4 ms: 1.46x faster                                  |
| float                   | 72.3 ms                                                | 49.7 ms: 1.46x faster                                  |
| scimark_monte_carlo     | 72.2 ms                                                | 50.0 ms: 1.44x faster                                  |
| async_tree_none         | 402 ms                                                 | 278 ms: 1.44x faster                                   |
| async_tree_io           | 1.02 sec                                               | 726 ms: 1.40x faster                                   |
| pyflate                 | 453 ms                                                 | 324 ms: 1.40x faster                                   |
| deepcopy_memo           | 34.5 us                                                | 24.7 us: 1.39x faster                                  |
| json_dumps              | 8.38 ms                                                | 6.06 ms: 1.38x faster                                  |
| pycparser               | 915 ms                                                 | 664 ms: 1.38x faster                                   |
| genshi_xml              | 37.6 ms                                                | 27.5 ms: 1.37x faster                                  |
| regex_compile           | 96.6 ms                                                | 71.0 ms: 1.36x faster                                  |
| pprint_pformat          | 1.24 sec                                               | 920 ms: 1.35x faster                                   |
| python_startup          | 12.6 ms                                                | 9.36 ms: 1.35x faster                                  |
| pprint_safe_repr        | 609 ms                                                 | 452 ms: 1.35x faster                                   |
| chameleon               | 5.84 ms                                                | 4.34 ms: 1.35x faster                                  |
| tornado_http            | 91.9 ms                                                | 68.4 ms: 1.34x faster                                  |
| genshi_text             | 18.4 ms                                                | 13.8 ms: 1.33x faster                                  |
| pathlib                 | 28.8 ms                                                | 21.8 ms: 1.32x faster                                  |
| logging_format          | 5.01 us                                                | 3.80 us: 1.32x faster                                  |
| sqlglot_parse           | 1.33 ms                                                | 1.01 ms: 1.32x faster                                  |
| python_startup_no_site  | 9.73 ms                                                | 7.38 ms: 1.32x faster                                  |
| logging_simple          | 4.63 us                                                | 3.51 us: 1.32x faster                                  |
| django_template         | 27.3 ms                                                | 20.8 ms: 1.32x faster                                  |
| spectral_norm           | 96.4 ms                                                | 73.4 ms: 1.31x faster                                  |
| thrift                  | 586 us                                                 | 447 us: 1.31x faster                                   |
| dulwich_log             | 37.1 ms                                                | 28.4 ms: 1.31x faster                                  |
| sqlglot_transpile       | 1.54 ms                                                | 1.18 ms: 1.30x faster                                  |
| deepcopy                | 278 us                                                 | 215 us: 1.29x faster                                   |
| deepcopy_reduce         | 2.38 us                                                | 1.86 us: 1.28x faster                                  |
| xml_etree_process       | 45.1 ms                                                | 35.2 ms: 1.28x faster                                  |
| create_gc_cycles        | 876 us                                                 | 687 us: 1.28x faster                                   |
| sqlalchemy_imperative   | 9.03 ms                                                | 7.12 ms: 1.27x faster                                  |
| unpack_sequence         | 38.7 ns                                                | 30.6 ns: 1.27x faster                                  |
| fannkuch                | 317 ms                                                 | 251 ms: 1.26x faster                                   |
| html5lib                | 44.1 ms                                                | 35.0 ms: 1.26x faster                                  |
| async_tree_cpu_io_mixed | 670 ms                                                 | 534 ms: 1.25x faster                                   |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.77 ms: 1.25x faster                                  |
| bench_thread_pool       | 548 us                                                 | 444 us: 1.23x faster                                   |
| scimark_fft             | 232 ms                                                 | 189 ms: 1.23x faster                                   |
| sqlglot_optimize        | 38.0 ms                                                | 31.1 ms: 1.22x faster                                  |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.22x faster                                 |
| sympy_integrate         | 13.4 ms                                                | 11.1 ms: 1.20x faster                                  |
| sqlalchemy_declarative  | 74.8 ms                                                | 62.7 ms: 1.19x faster                                  |
| sympy_str               | 169 ms                                                 | 144 ms: 1.17x faster                                   |
| sqlglot_normalize       | 197 ms                                                 | 169 ms: 1.16x faster                                   |
| sympy_expand            | 276 ms                                                 | 238 ms: 1.16x faster                                   |
| xml_etree_parse         | 107 ms                                                 | 93.0 ms: 1.15x faster                                  |
| sympy_sum               | 94.3 ms                                                | 82.1 ms: 1.15x faster                                  |
| nqueens                 | 68.1 ms                                                | 59.5 ms: 1.14x faster                                  |
| mypy2                   | 308 ms                                                 | 271 ms: 1.14x faster                                   |
| 2to3                    | 202 ms                                                 | 181 ms: 1.12x faster                                   |
| mdp                     | 1.67 sec                                               | 1.51 sec: 1.10x faster                                 |
| xml_etree_generate      | 54.3 ms                                                | 49.2 ms: 1.10x faster                                  |
| coroutines              | 20.2 ms                                                | 18.4 ms: 1.10x faster                                  |
| json                    | 3.10 ms                                                | 2.83 ms: 1.09x faster                                  |
| regex_v8                | 17.5 ms                                                | 16.0 ms: 1.09x faster                                  |
| telco                   | 3.68 ms                                                | 3.38 ms: 1.09x faster                                  |
| xml_etree_iterparse     | 72.6 ms                                                | 67.1 ms: 1.08x faster                                  |
| meteor_contest          | 78.6 ms                                                | 72.7 ms: 1.08x faster                                  |
| sqlite_synth            | 1.47 us                                                | 1.37 us: 1.08x faster                                  |
| regex_dna               | 160 ms                                                 | 150 ms: 1.07x faster                                   |
| json_loads              | 16.9 us                                                | 16.3 us: 1.03x faster                                  |
| gc_traversal            | 2.40 ms                                                | 2.41 ms: 1.00x slower                                  |
| unpickle_list           | 2.66 us                                                | 2.67 us: 1.00x slower                                  |
| pickle_dict             | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| unpickle                | 9.77 us                                                | 9.91 us: 1.01x slower                                  |
| pickle                  | 7.36 us                                                | 7.57 us: 1.03x slower                                  |
| bench_mp_pool           | 41.0 ms                                                | 42.6 ms: 1.04x slower                                  |
| regex_effbot            | 2.45 ms                                                | 2.60 ms: 1.06x slower                                  |
| async_generators        | 233 ms                                                 | 255 ms: 1.09x slower                                   |
| coverage                | 40.8 ms                                                | 60.3 ms: 1.48x slower                                  |
| Geometric mean          | (ref)                                                  | 1.25x faster                                           |

Benchmark hidden because not significant (3): generators, pickle_list, pidigits
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, comprehensions, dask, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x
