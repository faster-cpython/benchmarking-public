
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_call
- machine: linux-x86_64
- commit hash: 29928ee
- commit date: 2023-03-25
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                |
| chameleon      | 9.06 ms                                                | 6.55 ms: 1.38x faster                                               |
| docutils       | 3.17 sec                                               | 2.54 sec: 1.25x faster                                              |
| html5lib       | 85.9 ms                                                | 61.5 ms: 1.40x faster                                               |
| tornado_http   | 127 ms                                                 | 91.4 ms: 1.39x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.9 ms: 1.61x faster                                               |
| float          | 111 ms                                                 | 74.7 ms: 1.48x faster                                               |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.34x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.4 ms: 1.17x faster                                               |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                                |
| regex_effbot   | 3.23 ms                                                | 3.45 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.11x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 288 us: 1.58x faster                                                |
| unpickle_pure_python | 300 us                                                 | 202 us: 1.49x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.48 ms: 1.43x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 55.9 ms: 1.34x faster                                               |
| json_loads           | 28.8 us                                                | 24.4 us: 1.18x faster                                               |
| xml_etree_generate   | 94.2 ms                                                | 81.4 ms: 1.16x faster                                               |
| pickle_list          | 4.56 us                                                | 4.12 us: 1.11x faster                                               |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.10x faster                                                |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                                |
| unpickle             | 14.1 us                                                | 13.6 us: 1.04x faster                                               |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                               |
| unpickle_list        | 4.82 us                                                | 5.23 us: 1.08x slower                                               |
| pickle_dict          | 27.3 us                                                | 30.7 us: 1.13x slower                                               |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.85 ms: 1.60x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.55 ms: 1.13x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.98 ms: 1.48x faster                                               |
| genshi_text     | 30.3 ms                                                | 21.2 ms: 1.43x faster                                               |
| django_template | 45.9 ms                                                | 33.3 ms: 1.38x faster                                               |
| genshi_xml      | 63.3 ms                                                | 46.9 ms: 1.35x faster                                               |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.2 ms: 2.54x faster                                               |
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                               |
| asyncio_tcp             | 925 ms                                                 | 504 ms: 1.84x faster                                                |
| logging_silent          | 175 ns                                                 | 97.0 ns: 1.80x faster                                               |
| scimark_sor             | 197 ms                                                 | 112 ms: 1.76x faster                                                |
| richards                | 74.9 ms                                                | 44.2 ms: 1.70x faster                                               |
| go                      | 229 ms                                                 | 138 ms: 1.67x faster                                                |
| raytrace                | 464 ms                                                 | 285 ms: 1.63x faster                                                |
| scimark_monte_carlo     | 108 ms                                                 | 66.7 ms: 1.62x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 73.1 ms: 1.62x faster                                               |
| chaos                   | 106 ms                                                 | 65.8 ms: 1.61x faster                                               |
| nbody                   | 142 ms                                                 | 87.9 ms: 1.61x faster                                               |
| python_startup          | 14.2 ms                                                | 8.85 ms: 1.60x faster                                               |
| pickle_pure_python      | 455 us                                                 | 288 us: 1.58x faster                                                |
| hexiom                  | 9.53 ms                                                | 6.03 ms: 1.58x faster                                               |
| pyflate                 | 673 ms                                                 | 431 ms: 1.56x faster                                                |
| deepcopy_memo           | 52.3 us                                                | 33.7 us: 1.55x faster                                               |
| spectral_norm           | 150 ms                                                 | 97.3 ms: 1.54x faster                                               |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.52x faster                                                |
| unpickle_pure_python    | 300 us                                                 | 202 us: 1.49x faster                                                |
| float                   | 111 ms                                                 | 74.7 ms: 1.48x faster                                               |
| mako                    | 14.8 ms                                                | 9.98 ms: 1.48x faster                                               |
| unpack_sequence         | 64.7 ns                                                | 44.0 ns: 1.47x faster                                               |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.43x faster                                               |
| genshi_text             | 30.3 ms                                                | 21.2 ms: 1.43x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.48 ms: 1.43x faster                                               |
| sqlglot_transpile       | 2.45 ms                                                | 1.73 ms: 1.41x faster                                               |
| logging_simple          | 8.07 us                                                | 5.73 us: 1.41x faster                                               |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.40x faster                                              |
| logging_format          | 8.91 us                                                | 6.36 us: 1.40x faster                                               |
| html5lib                | 85.9 ms                                                | 61.5 ms: 1.40x faster                                               |
| tornado_http            | 127 ms                                                 | 91.4 ms: 1.39x faster                                               |
| pprint_safe_repr        | 955 ms                                                 | 686 ms: 1.39x faster                                                |
| chameleon               | 9.06 ms                                                | 6.55 ms: 1.38x faster                                               |
| django_template         | 45.9 ms                                                | 33.3 ms: 1.38x faster                                               |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.37x faster                                              |
| async_tree_none         | 717 ms                                                 | 522 ms: 1.37x faster                                                |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                               |
| scimark_fft             | 424 ms                                                 | 310 ms: 1.37x faster                                                |
| coroutines              | 31.8 ms                                                | 23.5 ms: 1.36x faster                                               |
| deepcopy                | 442 us                                                 | 327 us: 1.35x faster                                                |
| genshi_xml              | 63.3 ms                                                | 46.9 ms: 1.35x faster                                               |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                               |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                |
| xml_etree_process       | 74.9 ms                                                | 55.9 ms: 1.34x faster                                               |
| async_tree_memoization  | 854 ms                                                 | 638 ms: 1.34x faster                                                |
| thrift                  | 1.03 ms                                                | 783 us: 1.32x faster                                                |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.31x faster                                              |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.18 ms: 1.30x faster                                               |
| deepcopy_reduce         | 3.82 us                                                | 2.96 us: 1.29x faster                                               |
| async_tree_cpu_io_mixed | 951 ms                                                 | 739 ms: 1.29x faster                                                |
| mypy2                   | 428 ms                                                 | 333 ms: 1.29x faster                                                |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 51.5 ms: 1.27x faster                                               |
| fannkuch                | 486 ms                                                 | 384 ms: 1.26x faster                                                |
| docutils                | 3.17 sec                                               | 2.54 sec: 1.25x faster                                              |
| nqueens                 | 100 ms                                                 | 80.6 ms: 1.24x faster                                               |
| bench_thread_pool       | 947 us                                                 | 784 us: 1.21x faster                                                |
| dulwich_log             | 75.9 ms                                                | 63.5 ms: 1.20x faster                                               |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.19x faster                                               |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.9 ms: 1.19x faster                                               |
| sqlalchemy_declarative  | 165 ms                                                 | 140 ms: 1.18x faster                                                |
| json_loads              | 28.8 us                                                | 24.4 us: 1.18x faster                                               |
| sympy_expand            | 545 ms                                                 | 462 ms: 1.18x faster                                                |
| regex_v8                | 25.0 ms                                                | 21.4 ms: 1.17x faster                                               |
| json                    | 5.42 ms                                                | 4.65 ms: 1.17x faster                                               |
| xml_etree_generate      | 94.2 ms                                                | 81.4 ms: 1.16x faster                                               |
| sympy_str               | 328 ms                                                 | 285 ms: 1.15x faster                                                |
| pathlib                 | 20.0 ms                                                | 17.4 ms: 1.15x faster                                               |
| comprehensions          | 26.8 us                                                | 23.7 us: 1.13x faster                                               |
| mdp                     | 2.82 sec                                               | 2.50 sec: 1.13x faster                                              |
| sqlite_synth            | 2.93 us                                                | 2.61 us: 1.12x faster                                               |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.11x faster                                               |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                               |
| sympy_sum               | 185 ms                                                 | 167 ms: 1.11x faster                                                |
| pickle_list             | 4.56 us                                                | 4.12 us: 1.11x faster                                               |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.10x faster                                                |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                                |
| regex_dna               | 222 ms                                                 | 207 ms: 1.07x faster                                                |
| async_generators        | 425 ms                                                 | 408 ms: 1.04x faster                                                |
| unpickle                | 14.1 us                                                | 13.6 us: 1.04x faster                                               |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                               |
| gc_traversal            | 3.84 ms                                                | 3.83 ms: 1.00x faster                                               |
| regex_effbot            | 3.23 ms                                                | 3.45 ms: 1.07x slower                                               |
| unpickle_list           | 4.82 us                                                | 5.23 us: 1.08x slower                                               |
| python_startup_no_site  | 5.82 ms                                                | 6.55 ms: 1.13x slower                                               |
| pickle_dict             | 27.3 us                                                | 30.7 us: 1.13x slower                                               |
| dask                    | 423 ms                                                 | 512 ms: 1.21x slower                                                |
| coverage                | 72.8 ms                                                | 99.1 ms: 1.36x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (2): bench_mp_pool, telco
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
