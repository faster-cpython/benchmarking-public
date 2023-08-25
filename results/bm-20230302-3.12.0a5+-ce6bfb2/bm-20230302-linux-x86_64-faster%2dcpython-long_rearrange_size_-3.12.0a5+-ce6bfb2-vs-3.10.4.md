
# Results vs. 3.10.4

- fork: faster-cpython
- ref: long_rearrange_size_
- machine: linux-x86_64
- commit hash: ce6bfb2
- commit date: 2023-03-02
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                             |
| chameleon      | 9.06 ms                                                | 6.43 ms: 1.41x faster                                                            |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                           |
| html5lib       | 85.9 ms                                                | 61.8 ms: 1.39x faster                                                            |
| tornado_http   | 127 ms                                                 | 95.0 ms: 1.34x faster                                                            |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 91.6 ms: 1.55x faster                                                            |
| float          | 111 ms                                                 | 74.6 ms: 1.48x faster                                                            |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                             |
| regex_v8       | 25.0 ms                                                | 21.5 ms: 1.17x faster                                                            |
| regex_dna      | 222 ms                                                 | 219 ms: 1.01x faster                                                             |
| regex_effbot   | 3.23 ms                                                | 3.44 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 285 us: 1.60x faster                                                             |
| unpickle_pure_python | 300 us                                                 | 200 us: 1.50x faster                                                             |
| json_dumps           | 13.5 ms                                                | 9.41 ms: 1.44x faster                                                            |
| xml_etree_process    | 74.9 ms                                                | 55.7 ms: 1.35x faster                                                            |
| json_loads           | 28.8 us                                                | 23.9 us: 1.21x faster                                                            |
| xml_etree_generate   | 94.2 ms                                                | 80.8 ms: 1.17x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| pickle_list          | 4.56 us                                                | 4.15 us: 1.10x faster                                                            |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.09x faster                                                             |
| unpickle             | 14.1 us                                                | 13.6 us: 1.04x faster                                                            |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                                            |
| unpickle_list        | 4.82 us                                                | 5.00 us: 1.04x slower                                                            |
| pickle_dict          | 27.3 us                                                | 30.9 us: 1.13x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.02 ms: 1.57x faster                                                            |
| python_startup_no_site | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.86 ms: 1.50x faster                                                            |
| genshi_text     | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                            |
| django_template | 45.9 ms                                                | 32.7 ms: 1.40x faster                                                            |
| genshi_xml      | 63.3 ms                                                | 48.2 ms: 1.31x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 31.0 ms: 2.48x faster                                                            |
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                                            |
| logging_silent          | 175 ns                                                 | 94.3 ns: 1.86x faster                                                            |
| asyncio_tcp             | 925 ms                                                 | 509 ms: 1.82x faster                                                             |
| scimark_sor             | 197 ms                                                 | 110 ms: 1.79x faster                                                             |
| richards                | 74.9 ms                                                | 43.9 ms: 1.71x faster                                                            |
| go                      | 229 ms                                                 | 136 ms: 1.69x faster                                                             |
| pyflate                 | 673 ms                                                 | 409 ms: 1.64x faster                                                             |
| scimark_monte_carlo     | 108 ms                                                 | 67.1 ms: 1.61x faster                                                            |
| raytrace                | 464 ms                                                 | 289 ms: 1.61x faster                                                             |
| pickle_pure_python      | 455 us                                                 | 285 us: 1.60x faster                                                             |
| crypto_pyaes            | 118 ms                                                 | 74.5 ms: 1.59x faster                                                            |
| chaos                   | 106 ms                                                 | 67.6 ms: 1.57x faster                                                            |
| python_startup          | 14.2 ms                                                | 9.02 ms: 1.57x faster                                                            |
| nbody                   | 142 ms                                                 | 91.6 ms: 1.55x faster                                                            |
| unpack_sequence         | 64.7 ns                                                | 41.9 ns: 1.55x faster                                                            |
| hexiom                  | 9.53 ms                                                | 6.21 ms: 1.53x faster                                                            |
| spectral_norm           | 150 ms                                                 | 98.4 ms: 1.52x faster                                                            |
| deepcopy_memo           | 52.3 us                                                | 34.4 us: 1.52x faster                                                            |
| unpickle_pure_python    | 300 us                                                 | 200 us: 1.50x faster                                                             |
| mako                    | 14.8 ms                                                | 9.86 ms: 1.50x faster                                                            |
| float                   | 111 ms                                                 | 74.6 ms: 1.48x faster                                                            |
| scimark_lu              | 163 ms                                                 | 111 ms: 1.47x faster                                                             |
| json_dumps              | 13.5 ms                                                | 9.41 ms: 1.44x faster                                                            |
| sqlglot_parse           | 2.06 ms                                                | 1.43 ms: 1.44x faster                                                            |
| genshi_text             | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                            |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                                           |
| pprint_safe_repr        | 955 ms                                                 | 672 ms: 1.42x faster                                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.73 ms: 1.42x faster                                                            |
| logging_format          | 8.91 us                                                | 6.30 us: 1.41x faster                                                            |
| chameleon               | 9.06 ms                                                | 6.43 ms: 1.41x faster                                                            |
| django_template         | 45.9 ms                                                | 32.7 ms: 1.40x faster                                                            |
| logging_simple          | 8.07 us                                                | 5.78 us: 1.40x faster                                                            |
| html5lib                | 85.9 ms                                                | 61.8 ms: 1.39x faster                                                            |
| coroutines              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                            |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                                           |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                                             |
| fannkuch                | 486 ms                                                 | 360 ms: 1.35x faster                                                             |
| xml_etree_process       | 74.9 ms                                                | 55.7 ms: 1.35x faster                                                            |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                             |
| tornado_http            | 127 ms                                                 | 95.0 ms: 1.34x faster                                                            |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                            |
| deepcopy                | 442 us                                                 | 331 us: 1.33x faster                                                             |
| thrift                  | 1.03 ms                                                | 781 us: 1.32x faster                                                             |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.32x faster                                                           |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                             |
| genshi_xml              | 63.3 ms                                                | 48.2 ms: 1.31x faster                                                            |
| scimark_fft             | 424 ms                                                 | 324 ms: 1.31x faster                                                             |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 661 ms: 1.29x faster                                                             |
| mypy2                   | 428 ms                                                 | 333 ms: 1.29x faster                                                             |
| async_tree_cpu_io_mixed | 951 ms                                                 | 744 ms: 1.28x faster                                                             |
| sqlglot_optimize        | 65.3 ms                                                | 51.2 ms: 1.28x faster                                                            |
| deepcopy_reduce         | 3.82 us                                                | 3.01 us: 1.27x faster                                                            |
| nqueens                 | 100 ms                                                 | 80.4 ms: 1.24x faster                                                            |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                           |
| json_loads              | 28.8 us                                                | 23.9 us: 1.21x faster                                                            |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                                             |
| dulwich_log             | 75.9 ms                                                | 63.8 ms: 1.19x faster                                                            |
| json                    | 5.42 ms                                                | 4.57 ms: 1.19x faster                                                            |
| sympy_expand            | 545 ms                                                 | 460 ms: 1.18x faster                                                             |
| bench_thread_pool       | 947 us                                                 | 800 us: 1.18x faster                                                             |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.9 ms: 1.18x faster                                                            |
| sympy_integrate         | 24.3 ms                                                | 20.6 ms: 1.18x faster                                                            |
| xml_etree_generate      | 94.2 ms                                                | 80.8 ms: 1.17x faster                                                            |
| regex_v8                | 25.0 ms                                                | 21.5 ms: 1.17x faster                                                            |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.71 ms: 1.16x faster                                                            |
| sympy_str               | 328 ms                                                 | 286 ms: 1.15x faster                                                             |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.13x faster                                                            |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.13x faster                                                            |
| mdp                     | 2.82 sec                                               | 2.50 sec: 1.13x faster                                                           |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                                            |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.12x faster                                                             |
| comprehensions          | 26.8 us                                                | 24.1 us: 1.11x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| djangocms               | 35.9 us                                                | 32.5 us: 1.10x faster                                                            |
| sympy_sum               | 185 ms                                                 | 167 ms: 1.10x faster                                                             |
| pickle_list             | 4.56 us                                                | 4.15 us: 1.10x faster                                                            |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.09x faster                                                             |
| unpickle                | 14.1 us                                                | 13.6 us: 1.04x faster                                                            |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                                            |
| regex_dna               | 222 ms                                                 | 219 ms: 1.01x faster                                                             |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                             |
| async_generators        | 425 ms                                                 | 421 ms: 1.01x faster                                                             |
| telco                   | 6.54 ms                                                | 6.50 ms: 1.01x faster                                                            |
| unpickle_list           | 4.82 us                                                | 5.00 us: 1.04x slower                                                            |
| gc_traversal            | 3.84 ms                                                | 4.07 ms: 1.06x slower                                                            |
| regex_effbot            | 3.23 ms                                                | 3.44 ms: 1.07x slower                                                            |
| python_startup_no_site  | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                            |
| pickle_dict             | 27.3 us                                                | 30.9 us: 1.13x slower                                                            |
| dask                    | 423 ms                                                 | 505 ms: 1.19x slower                                                             |
| coverage                | 72.8 ms                                                | 95.7 ms: 1.31x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                     |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
