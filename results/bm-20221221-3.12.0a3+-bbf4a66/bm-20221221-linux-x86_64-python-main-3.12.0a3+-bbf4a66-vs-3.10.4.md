
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: bbf4a66
- commit date: 2022-12-21
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                   |
| chameleon      | 9.17 ms                                                | 6.35 ms: 1.44x faster                                  |
| docutils       | 3.18 sec                                               | 2.49 sec: 1.28x faster                                 |
| html5lib       | 85.9 ms                                                | 59.2 ms: 1.45x faster                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.4 ms: 1.52x faster                                  |
| float          | 109 ms                                                 | 71.9 ms: 1.52x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.38x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                  |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.47 ms: 1.09x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 282 us: 1.60x faster                                   |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.49 ms: 1.42x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 54.2 ms: 1.37x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 77.2 ms: 1.21x faster                                  |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                  |
| pickle_list          | 4.72 us                                                | 4.17 us: 1.13x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 146 ms: 1.11x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| pickle               | 10.2 us                                                | 10.2 us: 1.01x slower                                  |
| unpickle_list        | 4.92 us                                                | 5.01 us: 1.02x slower                                  |
| pickle_dict          | 27.6 us                                                | 30.9 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.41 ms: 1.68x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.07 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.26x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.46 ms: 1.55x faster                                  |
| genshi_text     | 30.6 ms                                                | 20.0 ms: 1.53x faster                                  |
| django_template | 46.3 ms                                                | 32.3 ms: 1.43x faster                                  |
| genshi_xml      | 63.7 ms                                                | 46.3 ms: 1.38x faster                                  |
| Geometric mean  | (ref)                                                  | 1.47x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.27x faster                                  |
| logging_silent          | 176 ns                                                 | 93.0 ns: 1.90x faster                                  |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.88x faster                                   |
| richards                | 75.2 ms                                                | 41.7 ms: 1.80x faster                                  |
| go                      | 226 ms                                                 | 131 ms: 1.72x faster                                   |
| pyflate                 | 676 ms                                                 | 395 ms: 1.71x faster                                   |
| python_startup          | 14.1 ms                                                | 8.41 ms: 1.68x faster                                  |
| scimark_monte_carlo     | 109 ms                                                 | 65.5 ms: 1.66x faster                                  |
| raytrace                | 467 ms                                                 | 282 ms: 1.65x faster                                   |
| pickle_pure_python      | 452 us                                                 | 282 us: 1.60x faster                                   |
| spectral_norm           | 150 ms                                                 | 93.6 ms: 1.60x faster                                  |
| chaos                   | 106 ms                                                 | 66.6 ms: 1.59x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 74.8 ms: 1.56x faster                                  |
| mako                    | 14.7 ms                                                | 9.46 ms: 1.55x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.09 ms: 1.55x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                   |
| deepcopy_memo           | 51.7 us                                                | 33.7 us: 1.53x faster                                  |
| genshi_text             | 30.6 ms                                                | 20.0 ms: 1.53x faster                                  |
| scimark_lu              | 161 ms                                                 | 105 ms: 1.53x faster                                   |
| nbody                   | 144 ms                                                 | 94.4 ms: 1.52x faster                                  |
| float                   | 109 ms                                                 | 71.9 ms: 1.52x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.38 ms: 1.48x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.67 ms: 1.45x faster                                  |
| html5lib                | 85.9 ms                                                | 59.2 ms: 1.45x faster                                  |
| chameleon               | 9.17 ms                                                | 6.35 ms: 1.44x faster                                  |
| django_template         | 46.3 ms                                                | 32.3 ms: 1.43x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.43x faster                                 |
| logging_simple          | 8.10 us                                                | 5.69 us: 1.42x faster                                  |
| json_dumps              | 13.4 ms                                                | 9.49 ms: 1.42x faster                                  |
| pprint_safe_repr        | 953 ms                                                 | 675 ms: 1.41x faster                                   |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.41x faster                                 |
| logging_format          | 8.85 us                                                | 6.33 us: 1.40x faster                                  |
| thrift                  | 1.03 ms                                                | 744 us: 1.39x faster                                   |
| regex_compile           | 177 ms                                                 | 129 ms: 1.38x faster                                   |
| genshi_xml              | 63.7 ms                                                | 46.3 ms: 1.38x faster                                  |
| unpack_sequence         | 59.4 ns                                                | 43.2 ns: 1.37x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 54.2 ms: 1.37x faster                                  |
| scimark_fft             | 421 ms                                                 | 310 ms: 1.36x faster                                   |
| fannkuch                | 488 ms                                                 | 362 ms: 1.35x faster                                   |
| async_tree_none         | 711 ms                                                 | 533 ms: 1.33x faster                                   |
| async_tree_io           | 1.78 sec                                               | 1.34 sec: 1.33x faster                                 |
| deepcopy                | 438 us                                                 | 329 us: 1.33x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.10 ms: 1.33x faster                                  |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                   |
| deepcopy_reduce         | 3.79 us                                                | 2.88 us: 1.31x faster                                  |
| sqlglot_optimize        | 65.2 ms                                                | 49.9 ms: 1.31x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 103 ms: 1.31x faster                                   |
| async_tree_memoization  | 855 ms                                                 | 656 ms: 1.30x faster                                   |
| docutils                | 3.18 sec                                               | 2.49 sec: 1.28x faster                                 |
| nqueens                 | 100 ms                                                 | 78.6 ms: 1.27x faster                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 763 ms: 1.24x faster                                   |
| dulwich_log             | 75.8 ms                                                | 61.6 ms: 1.23x faster                                  |
| coroutines              | 31.6 ms                                                | 25.8 ms: 1.23x faster                                  |
| bench_thread_pool       | 946 us                                                 | 775 us: 1.22x faster                                   |
| xml_etree_generate      | 93.8 ms                                                | 77.2 ms: 1.21x faster                                  |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                  |
| async_generators        | 426 ms                                                 | 356 ms: 1.20x faster                                   |
| sympy_expand            | 534 ms                                                 | 447 ms: 1.19x faster                                   |
| sympy_integrate         | 24.0 ms                                                | 20.1 ms: 1.19x faster                                  |
| sympy_str               | 325 ms                                                 | 277 ms: 1.17x faster                                   |
| json                    | 5.35 ms                                                | 4.59 ms: 1.16x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.14x faster                                  |
| sympy_sum               | 183 ms                                                 | 161 ms: 1.14x faster                                   |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.14x faster                                  |
| pickle_list             | 4.72 us                                                | 4.17 us: 1.13x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 146 ms: 1.11x faster                                   |
| mdp                     | 2.74 sec                                               | 2.51 sec: 1.09x faster                                 |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| telco                   | 6.73 ms                                                | 6.23 ms: 1.08x faster                                  |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                   |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| pickle                  | 10.2 us                                                | 10.2 us: 1.01x slower                                  |
| unpickle_list           | 4.92 us                                                | 5.01 us: 1.02x slower                                  |
| generators              | 76.4 ms                                                | 78.3 ms: 1.02x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.07 ms: 1.05x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.47 ms: 1.09x slower                                  |
| pickle_dict             | 27.6 us                                                | 30.9 us: 1.12x slower                                  |
| coverage                | 74.7 ms                                                | 100 ms: 1.34x slower                                   |
| Geometric mean          | (ref)                                                  | 1.31x faster                                           |

Benchmark hidden because not significant (2): unpickle, bench_mp_pool
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221221-3.12.0a3+-bbf4a66/bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66.json: mypy
