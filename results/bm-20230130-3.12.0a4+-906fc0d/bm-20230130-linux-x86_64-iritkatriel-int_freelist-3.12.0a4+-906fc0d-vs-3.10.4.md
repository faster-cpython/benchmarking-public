
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 906fc0d
- commit date: 2023-01-30
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 253 ms: 1.32x faster                                                |
| chameleon      | 9.17 ms                                                | 6.31 ms: 1.45x faster                                               |
| docutils       | 3.18 sec                                               | 2.49 sec: 1.27x faster                                              |
| html5lib       | 85.9 ms                                                | 60.3 ms: 1.42x faster                                               |
| tornado_http   | 128 ms                                                 | 93.9 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                  | 1.37x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 109 ms                                                 | 72.1 ms: 1.51x faster                                               |
| nbody          | 144 ms                                                 | 95.5 ms: 1.51x faster                                               |
| pidigits       | 190 ms                                                 | 199 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                               |
| regex_dna      | 214 ms                                                 | 209 ms: 1.02x faster                                                |
| regex_effbot   | 3.19 ms                                                | 3.63 ms: 1.14x slower                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 287 us: 1.57x faster                                                |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                |
| json_dumps           | 13.4 ms                                                | 9.58 ms: 1.40x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 53.5 ms: 1.39x faster                                               |
| xml_etree_generate   | 93.8 ms                                                | 77.6 ms: 1.21x faster                                               |
| json_loads           | 28.7 us                                                | 24.2 us: 1.19x faster                                               |
| pickle_list          | 4.72 us                                                | 4.24 us: 1.11x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                               |
| unpickle_list        | 4.92 us                                                | 4.89 us: 1.01x faster                                               |
| pickle               | 10.2 us                                                | 10.2 us: 1.01x slower                                               |
| pickle_dict          | 27.6 us                                                | 31.2 us: 1.13x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.98 ms: 1.57x faster                                               |
| python_startup_no_site | 5.78 ms                                                | 6.49 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.87 ms: 1.48x faster                                               |
| genshi_text     | 30.6 ms                                                | 21.0 ms: 1.46x faster                                               |
| django_template | 46.3 ms                                                | 33.1 ms: 1.40x faster                                               |
| genshi_xml      | 63.7 ms                                                | 47.6 ms: 1.34x faster                                               |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.20 ms: 2.28x faster                                               |
| logging_silent          | 176 ns                                                 | 92.2 ns: 1.91x faster                                               |
| asyncio_tcp             | 914 ms                                                 | 494 ms: 1.85x faster                                                |
| richards                | 75.2 ms                                                | 41.6 ms: 1.81x faster                                               |
| scimark_sor             | 197 ms                                                 | 111 ms: 1.78x faster                                                |
| pyflate                 | 676 ms                                                 | 396 ms: 1.71x faster                                                |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                                |
| chaos                   | 106 ms                                                 | 63.9 ms: 1.65x faster                                               |
| scimark_monte_carlo     | 109 ms                                                 | 66.7 ms: 1.63x faster                                               |
| raytrace                | 467 ms                                                 | 289 ms: 1.62x faster                                                |
| hexiom                  | 9.43 ms                                                | 5.97 ms: 1.58x faster                                               |
| pickle_pure_python      | 452 us                                                 | 287 us: 1.57x faster                                                |
| python_startup          | 14.1 ms                                                | 8.98 ms: 1.57x faster                                               |
| crypto_pyaes            | 117 ms                                                 | 76.0 ms: 1.54x faster                                               |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                |
| scimark_lu              | 161 ms                                                 | 106 ms: 1.52x faster                                                |
| float                   | 109 ms                                                 | 72.1 ms: 1.51x faster                                               |
| nbody                   | 144 ms                                                 | 95.5 ms: 1.51x faster                                               |
| deepcopy_memo           | 51.7 us                                                | 34.6 us: 1.49x faster                                               |
| mako                    | 14.7 ms                                                | 9.87 ms: 1.48x faster                                               |
| genshi_text             | 30.6 ms                                                | 21.0 ms: 1.46x faster                                               |
| chameleon               | 9.17 ms                                                | 6.31 ms: 1.45x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                               |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.43x faster                                              |
| spectral_norm           | 150 ms                                                 | 105 ms: 1.43x faster                                                |
| logging_simple          | 8.10 us                                                | 5.68 us: 1.43x faster                                               |
| pprint_safe_repr        | 953 ms                                                 | 669 ms: 1.42x faster                                                |
| html5lib                | 85.9 ms                                                | 60.3 ms: 1.42x faster                                               |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                               |
| logging_format          | 8.85 us                                                | 6.30 us: 1.41x faster                                               |
| json_dumps              | 13.4 ms                                                | 9.58 ms: 1.40x faster                                               |
| django_template         | 46.3 ms                                                | 33.1 ms: 1.40x faster                                               |
| thrift                  | 1.03 ms                                                | 742 us: 1.39x faster                                                |
| xml_etree_process       | 74.5 ms                                                | 53.5 ms: 1.39x faster                                               |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                                |
| pycparser               | 1.53 sec                                               | 1.12 sec: 1.37x faster                                              |
| unpack_sequence         | 59.4 ns                                                | 43.3 ns: 1.37x faster                                               |
| tornado_http            | 128 ms                                                 | 93.9 ms: 1.36x faster                                               |
| fannkuch                | 488 ms                                                 | 358 ms: 1.36x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.02 ms: 1.36x faster                                               |
| scimark_fft             | 421 ms                                                 | 311 ms: 1.36x faster                                                |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.35x faster                                              |
| async_tree_none         | 711 ms                                                 | 525 ms: 1.35x faster                                                |
| aiohttp                 | 1.34 ms                                                | 997 us: 1.34x faster                                                |
| genshi_xml              | 63.7 ms                                                | 47.6 ms: 1.34x faster                                               |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                               |
| deepcopy                | 438 us                                                 | 330 us: 1.33x faster                                                |
| 2to3                    | 335 ms                                                 | 253 ms: 1.32x faster                                                |
| async_tree_memoization  | 855 ms                                                 | 658 ms: 1.30x faster                                                |
| deepcopy_reduce         | 3.79 us                                                | 2.94 us: 1.29x faster                                               |
| sqlglot_optimize        | 65.2 ms                                                | 51.2 ms: 1.28x faster                                               |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.27x faster                                                |
| docutils                | 3.18 sec                                               | 2.49 sec: 1.27x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 752 ms: 1.26x faster                                                |
| coroutines              | 31.6 ms                                                | 25.1 ms: 1.26x faster                                               |
| nqueens                 | 100 ms                                                 | 79.5 ms: 1.26x faster                                               |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.22x faster                                               |
| xml_etree_generate      | 93.8 ms                                                | 77.6 ms: 1.21x faster                                               |
| dulwich_log             | 75.8 ms                                                | 62.8 ms: 1.21x faster                                               |
| async_generators        | 426 ms                                                 | 353 ms: 1.21x faster                                                |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                                |
| bench_thread_pool       | 946 us                                                 | 790 us: 1.20x faster                                                |
| json_loads              | 28.7 us                                                | 24.2 us: 1.19x faster                                               |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                |
| sympy_expand            | 534 ms                                                 | 453 ms: 1.18x faster                                                |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                               |
| djangocms               | 36.9 us                                                | 32.1 us: 1.15x faster                                               |
| json                    | 5.35 ms                                                | 4.67 ms: 1.14x faster                                               |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                               |
| sqlite_synth            | 2.92 us                                                | 2.60 us: 1.12x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                               |
| pickle_list             | 4.72 us                                                | 4.24 us: 1.11x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                               |
| meteor_contest          | 114 ms                                                 | 107 ms: 1.06x faster                                                |
| telco                   | 6.73 ms                                                | 6.38 ms: 1.06x faster                                               |
| mdp                     | 2.74 sec                                               | 2.62 sec: 1.05x faster                                              |
| regex_dna               | 214 ms                                                 | 209 ms: 1.02x faster                                                |
| unpickle_list           | 4.92 us                                                | 4.89 us: 1.01x faster                                               |
| pickle                  | 10.2 us                                                | 10.2 us: 1.01x slower                                               |
| generators              | 76.4 ms                                                | 78.0 ms: 1.02x slower                                               |
| pidigits                | 190 ms                                                 | 199 ms: 1.05x slower                                                |
| gc_traversal            | 3.53 ms                                                | 3.82 ms: 1.08x slower                                               |
| python_startup_no_site  | 5.78 ms                                                | 6.49 ms: 1.12x slower                                               |
| pickle_dict             | 27.6 us                                                | 31.2 us: 1.13x slower                                               |
| regex_effbot            | 3.19 ms                                                | 3.63 ms: 1.14x slower                                               |
| dask                    | 436 ms                                                 | 498 ms: 1.14x slower                                                |
| coverage                | 74.7 ms                                                | 96.0 ms: 1.28x slower                                               |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                        |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230130-3.12.0a4+-906fc0d/bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d.json: mypy
