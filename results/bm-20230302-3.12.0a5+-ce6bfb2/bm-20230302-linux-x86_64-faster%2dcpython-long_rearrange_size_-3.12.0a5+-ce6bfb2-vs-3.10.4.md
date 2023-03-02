
# Results vs. 3.10.4

- fork: faster-cpython
- ref: long_rearrange_size_
- machine: linux-x86_64
- commit hash: ce6bfb2
- commit date: 2023-03-02
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                                             |
| chameleon      | 9.17 ms                                                | 6.43 ms: 1.43x faster                                                            |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.24x faster                                                           |
| html5lib       | 85.9 ms                                                | 61.8 ms: 1.39x faster                                                            |
| tornado_http   | 128 ms                                                 | 95.0 ms: 1.35x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 91.6 ms: 1.57x faster                                                            |
| float          | 109 ms                                                 | 74.6 ms: 1.46x faster                                                            |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                             |
| regex_v8       | 25.0 ms                                                | 21.5 ms: 1.17x faster                                                            |
| regex_dna      | 214 ms                                                 | 219 ms: 1.03x slower                                                             |
| regex_effbot   | 3.19 ms                                                | 3.44 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 285 us: 1.58x faster                                                             |
| unpickle_pure_python | 302 us                                                 | 200 us: 1.51x faster                                                             |
| json_dumps           | 13.4 ms                                                | 9.41 ms: 1.43x faster                                                            |
| xml_etree_process    | 74.5 ms                                                | 55.7 ms: 1.34x faster                                                            |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                                            |
| xml_etree_generate   | 93.8 ms                                                | 80.8 ms: 1.16x faster                                                            |
| pickle_list          | 4.72 us                                                | 4.15 us: 1.14x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                             |
| unpickle             | 14.2 us                                                | 13.6 us: 1.04x faster                                                            |
| unpickle_list        | 4.92 us                                                | 5.00 us: 1.02x slower                                                            |
| pickle_dict          | 27.6 us                                                | 30.9 us: 1.12x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.02 ms: 1.56x faster                                                            |
| python_startup_no_site | 5.78 ms                                                | 6.53 ms: 1.13x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.86 ms: 1.49x faster                                                            |
| genshi_text     | 30.6 ms                                                | 21.2 ms: 1.45x faster                                                            |
| django_template | 46.3 ms                                                | 32.7 ms: 1.41x faster                                                            |
| genshi_xml      | 63.7 ms                                                | 48.2 ms: 1.32x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 31.0 ms: 2.47x faster                                                            |
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.26x faster                                                            |
| logging_silent          | 176 ns                                                 | 94.3 ns: 1.87x faster                                                            |
| asyncio_tcp             | 914 ms                                                 | 509 ms: 1.80x faster                                                             |
| scimark_sor             | 197 ms                                                 | 110 ms: 1.79x faster                                                             |
| richards                | 75.2 ms                                                | 43.9 ms: 1.71x faster                                                            |
| go                      | 226 ms                                                 | 136 ms: 1.66x faster                                                             |
| pyflate                 | 676 ms                                                 | 409 ms: 1.65x faster                                                             |
| scimark_monte_carlo     | 109 ms                                                 | 67.1 ms: 1.62x faster                                                            |
| raytrace                | 467 ms                                                 | 289 ms: 1.62x faster                                                             |
| pickle_pure_python      | 452 us                                                 | 285 us: 1.58x faster                                                             |
| nbody                   | 144 ms                                                 | 91.6 ms: 1.57x faster                                                            |
| crypto_pyaes            | 117 ms                                                 | 74.5 ms: 1.57x faster                                                            |
| python_startup          | 14.1 ms                                                | 9.02 ms: 1.56x faster                                                            |
| chaos                   | 106 ms                                                 | 67.6 ms: 1.56x faster                                                            |
| spectral_norm           | 150 ms                                                 | 98.4 ms: 1.52x faster                                                            |
| hexiom                  | 9.43 ms                                                | 6.21 ms: 1.52x faster                                                            |
| unpickle_pure_python    | 302 us                                                 | 200 us: 1.51x faster                                                             |
| deepcopy_memo           | 51.7 us                                                | 34.4 us: 1.50x faster                                                            |
| mako                    | 14.7 ms                                                | 9.86 ms: 1.49x faster                                                            |
| float                   | 109 ms                                                 | 74.6 ms: 1.46x faster                                                            |
| scimark_lu              | 161 ms                                                 | 111 ms: 1.45x faster                                                             |
| genshi_text             | 30.6 ms                                                | 21.2 ms: 1.45x faster                                                            |
| json_dumps              | 13.4 ms                                                | 9.41 ms: 1.43x faster                                                            |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.43x faster                                                           |
| chameleon               | 9.17 ms                                                | 6.43 ms: 1.43x faster                                                            |
| sqlglot_parse           | 2.04 ms                                                | 1.43 ms: 1.43x faster                                                            |
| pprint_safe_repr        | 953 ms                                                 | 672 ms: 1.42x faster                                                             |
| unpack_sequence         | 59.4 ns                                                | 41.9 ns: 1.42x faster                                                            |
| django_template         | 46.3 ms                                                | 32.7 ms: 1.41x faster                                                            |
| sqlglot_transpile       | 2.43 ms                                                | 1.73 ms: 1.41x faster                                                            |
| logging_format          | 8.85 us                                                | 6.30 us: 1.41x faster                                                            |
| logging_simple          | 8.10 us                                                | 5.78 us: 1.40x faster                                                            |
| html5lib                | 85.9 ms                                                | 61.8 ms: 1.39x faster                                                            |
| coroutines              | 31.6 ms                                                | 23.1 ms: 1.37x faster                                                            |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                                           |
| fannkuch                | 488 ms                                                 | 360 ms: 1.36x faster                                                             |
| async_tree_none         | 711 ms                                                 | 526 ms: 1.35x faster                                                             |
| tornado_http            | 128 ms                                                 | 95.0 ms: 1.35x faster                                                            |
| pycparser               | 1.53 sec                                               | 1.14 sec: 1.34x faster                                                           |
| xml_etree_process       | 74.5 ms                                                | 55.7 ms: 1.34x faster                                                            |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                                             |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                            |
| thrift                  | 1.03 ms                                                | 781 us: 1.32x faster                                                             |
| genshi_xml              | 63.7 ms                                                | 48.2 ms: 1.32x faster                                                            |
| deepcopy                | 438 us                                                 | 331 us: 1.32x faster                                                             |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                             |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                            |
| scimark_fft             | 421 ms                                                 | 324 ms: 1.30x faster                                                             |
| async_tree_memoization  | 855 ms                                                 | 661 ms: 1.29x faster                                                             |
| mypy2                   | 430 ms                                                 | 333 ms: 1.29x faster                                                             |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                             |
| async_tree_cpu_io_mixed | 949 ms                                                 | 744 ms: 1.28x faster                                                             |
| sqlglot_optimize        | 65.2 ms                                                | 51.2 ms: 1.27x faster                                                            |
| deepcopy_reduce         | 3.79 us                                                | 3.01 us: 1.26x faster                                                            |
| nqueens                 | 100 ms                                                 | 80.4 ms: 1.24x faster                                                            |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.24x faster                                                           |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                                            |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.9 ms: 1.20x faster                                                            |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.19x faster                                                             |
| dulwich_log             | 75.8 ms                                                | 63.8 ms: 1.19x faster                                                            |
| bench_thread_pool       | 946 us                                                 | 800 us: 1.18x faster                                                             |
| json                    | 5.35 ms                                                | 4.57 ms: 1.17x faster                                                            |
| sympy_integrate         | 24.0 ms                                                | 20.6 ms: 1.17x faster                                                            |
| regex_v8                | 25.0 ms                                                | 21.5 ms: 1.17x faster                                                            |
| xml_etree_generate      | 93.8 ms                                                | 80.8 ms: 1.16x faster                                                            |
| sympy_expand            | 534 ms                                                 | 460 ms: 1.16x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.71 ms: 1.16x faster                                                            |
| pickle_list             | 4.72 us                                                | 4.15 us: 1.14x faster                                                            |
| sympy_str               | 325 ms                                                 | 286 ms: 1.14x faster                                                             |
| djangocms               | 36.9 us                                                | 32.5 us: 1.13x faster                                                            |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                            |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                                            |
| sqlite_synth            | 2.92 us                                                | 2.62 us: 1.12x faster                                                            |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                             |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| mdp                     | 2.74 sec                                               | 2.50 sec: 1.10x faster                                                           |
| sympy_sum               | 183 ms                                                 | 167 ms: 1.10x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                             |
| unpickle                | 14.2 us                                                | 13.6 us: 1.04x faster                                                            |
| telco                   | 6.73 ms                                                | 6.50 ms: 1.04x faster                                                            |
| async_generators        | 426 ms                                                 | 421 ms: 1.01x faster                                                             |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                             |
| unpickle_list           | 4.92 us                                                | 5.00 us: 1.02x slower                                                            |
| regex_dna               | 214 ms                                                 | 219 ms: 1.03x slower                                                             |
| regex_effbot            | 3.19 ms                                                | 3.44 ms: 1.08x slower                                                            |
| pickle_dict             | 27.6 us                                                | 30.9 us: 1.12x slower                                                            |
| python_startup_no_site  | 5.78 ms                                                | 6.53 ms: 1.13x slower                                                            |
| gc_traversal            | 3.53 ms                                                | 4.07 ms: 1.15x slower                                                            |
| dask                    | 436 ms                                                 | 505 ms: 1.16x slower                                                             |
| coverage                | 74.7 ms                                                | 95.7 ms: 1.28x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                     |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230302-3.12.0a5+-ce6bfb2/bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2.json: comprehensions
