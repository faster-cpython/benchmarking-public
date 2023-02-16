
# Results vs. 3.10.4

- fork: python
- ref: b724ac2fe7fbb5a7a33d
- machine: linux-x86_64
- commit hash: b724ac2
- commit date: 2023-01-23
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 253 ms: 1.33x faster                                                   |
| chameleon      | 9.17 ms                                                | 6.42 ms: 1.43x faster                                                  |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                 |
| html5lib       | 85.9 ms                                                | 60.3 ms: 1.42x faster                                                  |
| tornado_http   | 128 ms                                                 | 93.7 ms: 1.37x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.8 ms: 1.53x faster                                                  |
| float          | 109 ms                                                 | 72.6 ms: 1.50x faster                                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                  |
| regex_dna      | 214 ms                                                 | 201 ms: 1.06x faster                                                   |
| regex_effbot   | 3.19 ms                                                | 3.44 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 284 us: 1.59x faster                                                   |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                   |
| json_dumps           | 13.4 ms                                                | 9.38 ms: 1.43x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 54.4 ms: 1.37x faster                                                  |
| xml_etree_generate   | 93.8 ms                                                | 79.1 ms: 1.19x faster                                                  |
| json_loads           | 28.7 us                                                | 24.3 us: 1.18x faster                                                  |
| pickle_list          | 4.72 us                                                | 4.26 us: 1.11x faster                                                  |
| unpickle             | 14.2 us                                                | 13.4 us: 1.05x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.04x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.04x faster                                                   |
| pickle               | 10.2 us                                                | 10.3 us: 1.02x slower                                                  |
| unpickle_list        | 4.92 us                                                | 5.08 us: 1.03x slower                                                  |
| pickle_dict          | 27.6 us                                                | 32.2 us: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.96 ms: 1.57x faster                                                  |
| python_startup_no_site | 5.78 ms                                                | 6.49 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.66 ms: 1.52x faster                                                  |
| django_template | 46.3 ms                                                | 32.9 ms: 1.41x faster                                                  |
| genshi_text     | 30.6 ms                                                | 22.1 ms: 1.39x faster                                                  |
| genshi_xml      | 63.7 ms                                                | 46.8 ms: 1.36x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.23 ms: 2.25x faster                                                  |
| logging_silent          | 176 ns                                                 | 93.3 ns: 1.89x faster                                                  |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                                   |
| asyncio_tcp             | 914 ms                                                 | 490 ms: 1.86x faster                                                   |
| richards                | 75.2 ms                                                | 42.9 ms: 1.75x faster                                                  |
| pyflate                 | 676 ms                                                 | 400 ms: 1.69x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                 | 65.2 ms: 1.67x faster                                                  |
| raytrace                | 467 ms                                                 | 280 ms: 1.67x faster                                                   |
| go                      | 226 ms                                                 | 136 ms: 1.66x faster                                                   |
| chaos                   | 106 ms                                                 | 63.6 ms: 1.66x faster                                                  |
| crypto_pyaes            | 117 ms                                                 | 73.3 ms: 1.59x faster                                                  |
| pickle_pure_python      | 452 us                                                 | 284 us: 1.59x faster                                                   |
| hexiom                  | 9.43 ms                                                | 5.95 ms: 1.58x faster                                                  |
| python_startup          | 14.1 ms                                                | 8.96 ms: 1.57x faster                                                  |
| nbody                   | 144 ms                                                 | 93.8 ms: 1.53x faster                                                  |
| spectral_norm           | 150 ms                                                 | 97.7 ms: 1.53x faster                                                  |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                   |
| mako                    | 14.7 ms                                                | 9.66 ms: 1.52x faster                                                  |
| float                   | 109 ms                                                 | 72.6 ms: 1.50x faster                                                  |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.50x faster                                                   |
| deepcopy_memo           | 51.7 us                                                | 34.6 us: 1.49x faster                                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                                  |
| json_dumps              | 13.4 ms                                                | 9.38 ms: 1.43x faster                                                  |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.43x faster                                                 |
| chameleon               | 9.17 ms                                                | 6.42 ms: 1.43x faster                                                  |
| unpack_sequence         | 59.4 ns                                                | 41.6 ns: 1.43x faster                                                  |
| html5lib                | 85.9 ms                                                | 60.3 ms: 1.42x faster                                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                                  |
| pprint_safe_repr        | 953 ms                                                 | 674 ms: 1.41x faster                                                   |
| logging_simple          | 8.10 us                                                | 5.74 us: 1.41x faster                                                  |
| django_template         | 46.3 ms                                                | 32.9 ms: 1.41x faster                                                  |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.40x faster                                                 |
| logging_format          | 8.85 us                                                | 6.34 us: 1.40x faster                                                  |
| thrift                  | 1.03 ms                                                | 746 us: 1.39x faster                                                   |
| genshi_text             | 30.6 ms                                                | 22.1 ms: 1.39x faster                                                  |
| scimark_fft             | 421 ms                                                 | 306 ms: 1.37x faster                                                   |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                   |
| xml_etree_process       | 74.5 ms                                                | 54.4 ms: 1.37x faster                                                  |
| tornado_http            | 128 ms                                                 | 93.7 ms: 1.37x faster                                                  |
| genshi_xml              | 63.7 ms                                                | 46.8 ms: 1.36x faster                                                  |
| aiohttp                 | 1.34 ms                                                | 994 us: 1.35x faster                                                   |
| async_tree_none         | 711 ms                                                 | 528 ms: 1.35x faster                                                   |
| fannkuch                | 488 ms                                                 | 363 ms: 1.35x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.06 ms: 1.34x faster                                                  |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                                 |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                  |
| deepcopy                | 438 us                                                 | 327 us: 1.34x faster                                                   |
| 2to3                    | 335 ms                                                 | 253 ms: 1.33x faster                                                   |
| nqueens                 | 100 ms                                                 | 76.2 ms: 1.31x faster                                                  |
| async_tree_memoization  | 855 ms                                                 | 666 ms: 1.28x faster                                                   |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                   |
| deepcopy_reduce         | 3.79 us                                                | 2.97 us: 1.28x faster                                                  |
| sqlglot_optimize        | 65.2 ms                                                | 51.3 ms: 1.27x faster                                                  |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                 |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                                   |
| coroutines              | 31.6 ms                                                | 25.6 ms: 1.24x faster                                                  |
| dulwich_log             | 75.8 ms                                                | 62.0 ms: 1.22x faster                                                  |
| bench_thread_pool       | 946 us                                                 | 774 us: 1.22x faster                                                   |
| async_generators        | 426 ms                                                 | 351 ms: 1.21x faster                                                   |
| regex_v8                | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                  |
| sympy_integrate         | 24.0 ms                                                | 20.2 ms: 1.19x faster                                                  |
| xml_etree_generate      | 93.8 ms                                                | 79.1 ms: 1.19x faster                                                  |
| json_loads              | 28.7 us                                                | 24.3 us: 1.18x faster                                                  |
| sympy_expand            | 534 ms                                                 | 456 ms: 1.17x faster                                                   |
| djangocms               | 36.9 us                                                | 31.6 us: 1.17x faster                                                  |
| json                    | 5.35 ms                                                | 4.60 ms: 1.16x faster                                                  |
| sympy_str               | 325 ms                                                 | 281 ms: 1.16x faster                                                   |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.13x faster                                                  |
| mdp                     | 2.74 sec                                               | 2.43 sec: 1.13x faster                                                 |
| sympy_sum               | 183 ms                                                 | 164 ms: 1.12x faster                                                   |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                  |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.11x faster                                                  |
| pickle_list             | 4.72 us                                                | 4.26 us: 1.11x faster                                                  |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                   |
| regex_dna               | 214 ms                                                 | 201 ms: 1.06x faster                                                   |
| telco                   | 6.73 ms                                                | 6.38 ms: 1.06x faster                                                  |
| unpickle                | 14.2 us                                                | 13.4 us: 1.05x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 156 ms: 1.04x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.04x faster                                                   |
| generators              | 76.4 ms                                                | 74.7 ms: 1.02x faster                                                  |
| pickle                  | 10.2 us                                                | 10.3 us: 1.02x slower                                                  |
| unpickle_list           | 4.92 us                                                | 5.08 us: 1.03x slower                                                  |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| regex_effbot            | 3.19 ms                                                | 3.44 ms: 1.08x slower                                                  |
| gc_traversal            | 3.53 ms                                                | 3.96 ms: 1.12x slower                                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.49 ms: 1.12x slower                                                  |
| dask                    | 436 ms                                                 | 495 ms: 1.13x slower                                                   |
| pickle_dict             | 27.6 us                                                | 32.2 us: 1.17x slower                                                  |
| coverage                | 74.7 ms                                                | 97.3 ms: 1.30x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230123-3.12.0a4+-b724ac2/bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2.json: mypy
