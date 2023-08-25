
# Results vs. 3.10.4

- fork: iritkatriel
- ref: single_arg_exit
- machine: linux-x86_64
- commit hash: b560583
- commit date: 2023-02-17
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 246 ms: 1.36x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.29 ms: 1.44x faster                                                  |
| docutils       | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                 |
| html5lib       | 85.9 ms                                                | 61.7 ms: 1.39x faster                                                  |
| tornado_http   | 127 ms                                                 | 95.2 ms: 1.34x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.5 ms: 1.52x faster                                                  |
| nbody          | 142 ms                                                 | 93.1 ms: 1.52x faster                                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.17x faster                                                  |
| regex_dna      | 222 ms                                                 | 212 ms: 1.05x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.28 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 281 us: 1.62x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 196 us: 1.53x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.33 ms: 1.45x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 56.2 ms: 1.33x faster                                                  |
| json_loads           | 28.8 us                                                | 23.5 us: 1.22x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 80.7 ms: 1.17x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| pickle_list          | 4.56 us                                                | 4.18 us: 1.09x faster                                                  |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                                  |
| unpickle_list        | 4.82 us                                                | 5.08 us: 1.05x slower                                                  |
| pickle_dict          | 27.3 us                                                | 31.4 us: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.97 ms: 1.58x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.50 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.89 ms: 1.49x faster                                                  |
| genshi_text     | 30.3 ms                                                | 20.9 ms: 1.45x faster                                                  |
| django_template | 45.9 ms                                                | 33.6 ms: 1.37x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 48.0 ms: 1.32x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 31.3 ms: 2.45x faster                                                  |
| deltablue               | 7.42 ms                                                | 3.19 ms: 2.33x faster                                                  |
| logging_silent          | 175 ns                                                 | 92.1 ns: 1.90x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 501 ms: 1.85x faster                                                   |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                   |
| richards                | 74.9 ms                                                | 42.4 ms: 1.77x faster                                                  |
| go                      | 229 ms                                                 | 134 ms: 1.71x faster                                                   |
| scimark_monte_carlo     | 108 ms                                                 | 64.7 ms: 1.67x faster                                                  |
| pyflate                 | 673 ms                                                 | 408 ms: 1.65x faster                                                   |
| raytrace                | 464 ms                                                 | 283 ms: 1.64x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 72.6 ms: 1.63x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 281 us: 1.62x faster                                                   |
| spectral_norm           | 150 ms                                                 | 92.9 ms: 1.61x faster                                                  |
| chaos                   | 106 ms                                                 | 66.2 ms: 1.60x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.97 ms: 1.58x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 41.3 ns: 1.57x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.10 ms: 1.56x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 196 us: 1.53x faster                                                   |
| deepcopy_memo           | 52.3 us                                                | 34.3 us: 1.53x faster                                                  |
| float                   | 111 ms                                                 | 72.5 ms: 1.52x faster                                                  |
| nbody                   | 142 ms                                                 | 93.1 ms: 1.52x faster                                                  |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                                   |
| mako                    | 14.8 ms                                                | 9.89 ms: 1.49x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.33 ms: 1.45x faster                                                  |
| genshi_text             | 30.3 ms                                                | 20.9 ms: 1.45x faster                                                  |
| chameleon               | 9.06 ms                                                | 6.29 ms: 1.44x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.43 ms: 1.44x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.43x faster                                                 |
| pprint_safe_repr        | 955 ms                                                 | 670 ms: 1.43x faster                                                   |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.42x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.73 us: 1.41x faster                                                  |
| logging_format          | 8.91 us                                                | 6.34 us: 1.41x faster                                                  |
| coroutines              | 31.8 ms                                                | 22.7 ms: 1.40x faster                                                  |
| html5lib                | 85.9 ms                                                | 61.7 ms: 1.39x faster                                                  |
| scimark_fft             | 424 ms                                                 | 306 ms: 1.39x faster                                                   |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                                  |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                   |
| django_template         | 45.9 ms                                                | 33.6 ms: 1.37x faster                                                  |
| 2to3                    | 336 ms                                                 | 246 ms: 1.36x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.36x faster                                                 |
| thrift                  | 1.03 ms                                                | 759 us: 1.36x faster                                                   |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.36x faster                                                  |
| async_tree_none         | 717 ms                                                 | 529 ms: 1.35x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                                 |
| tornado_http            | 127 ms                                                 | 95.2 ms: 1.34x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.08 ms: 1.34x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 56.2 ms: 1.33x faster                                                  |
| fannkuch                | 486 ms                                                 | 366 ms: 1.33x faster                                                   |
| genshi_xml              | 63.3 ms                                                | 48.0 ms: 1.32x faster                                                  |
| deepcopy                | 442 us                                                 | 335 us: 1.32x faster                                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.93 us: 1.31x faster                                                  |
| mypy2                   | 428 ms                                                 | 329 ms: 1.30x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                   |
| nqueens                 | 100 ms                                                 | 77.6 ms: 1.29x faster                                                  |
| async_tree_memoization  | 854 ms                                                 | 663 ms: 1.29x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 745 ms: 1.28x faster                                                   |
| docutils                | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                 |
| json_loads              | 28.8 us                                                | 23.5 us: 1.22x faster                                                  |
| sympy_integrate         | 24.3 ms                                                | 19.9 ms: 1.22x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 62.6 ms: 1.21x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                   |
| sympy_str               | 328 ms                                                 | 272 ms: 1.21x faster                                                   |
| bench_thread_pool       | 947 us                                                 | 785 us: 1.21x faster                                                   |
| sympy_expand            | 545 ms                                                 | 455 ms: 1.20x faster                                                   |
| json                    | 5.42 ms                                                | 4.55 ms: 1.19x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.0 ms: 1.18x faster                                                  |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.17x faster                                                  |
| sympy_sum               | 185 ms                                                 | 158 ms: 1.17x faster                                                   |
| xml_etree_generate      | 94.2 ms                                                | 80.7 ms: 1.17x faster                                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.13x faster                                                  |
| sqlite_synth            | 2.93 us                                                | 2.63 us: 1.11x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                                   |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                   |
| djangocms               | 35.9 us                                                | 32.5 us: 1.10x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| pickle_list             | 4.56 us                                                | 4.18 us: 1.09x faster                                                  |
| gc_traversal            | 3.84 ms                                                | 3.53 ms: 1.09x faster                                                  |
| pathlib                 | 20.0 ms                                                | 18.4 ms: 1.09x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.62 sec: 1.08x faster                                                 |
| unpickle                | 14.1 us                                                | 13.1 us: 1.08x faster                                                  |
| regex_dna               | 222 ms                                                 | 212 ms: 1.05x faster                                                   |
| telco                   | 6.54 ms                                                | 6.29 ms: 1.04x faster                                                  |
| async_generators        | 425 ms                                                 | 412 ms: 1.03x faster                                                   |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| regex_effbot            | 3.23 ms                                                | 3.28 ms: 1.02x slower                                                  |
| unpickle_list           | 4.82 us                                                | 5.08 us: 1.05x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.50 ms: 1.12x slower                                                  |
| pickle_dict             | 27.3 us                                                | 31.4 us: 1.15x slower                                                  |
| dask                    | 423 ms                                                 | 499 ms: 1.18x slower                                                   |
| coverage                | 72.8 ms                                                | 96.4 ms: 1.32x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x
