
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: cfb886d
- commit date: 2023-02-10
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                |
| chameleon      | 9.17 ms                                                | 6.28 ms: 1.46x faster                                               |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                              |
| html5lib       | 85.9 ms                                                | 60.5 ms: 1.42x faster                                               |
| tornado_http   | 128 ms                                                 | 94.2 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 109 ms                                                 | 71.9 ms: 1.51x faster                                               |
| nbody          | 144 ms                                                 | 95.4 ms: 1.51x faster                                               |
| pidigits       | 190 ms                                                 | 203 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                  | 1.29x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.0 ms: 1.19x faster                                               |
| regex_dna      | 214 ms                                                 | 219 ms: 1.02x slower                                                |
| regex_effbot   | 3.19 ms                                                | 3.43 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.11x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 287 us: 1.58x faster                                                |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                |
| json_dumps           | 13.4 ms                                                | 9.57 ms: 1.40x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 55.7 ms: 1.34x faster                                               |
| json_loads           | 28.7 us                                                | 23.8 us: 1.21x faster                                               |
| xml_etree_generate   | 93.8 ms                                                | 80.8 ms: 1.16x faster                                               |
| pickle_list          | 4.72 us                                                | 4.09 us: 1.15x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.07x faster                                                |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                               |
| unpickle_list        | 4.92 us                                                | 4.87 us: 1.01x faster                                               |
| pickle_dict          | 27.6 us                                                | 30.9 us: 1.12x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.92 ms: 1.58x faster                                               |
| python_startup_no_site | 5.78 ms                                                | 6.48 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.81 ms: 1.49x faster                                               |
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.49x faster                                               |
| django_template | 46.3 ms                                                | 33.1 ms: 1.40x faster                                               |
| genshi_xml      | 63.7 ms                                                | 46.9 ms: 1.36x faster                                               |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.20 ms: 2.27x faster                                               |
| logging_silent          | 176 ns                                                 | 92.4 ns: 1.91x faster                                               |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                                |
| asyncio_tcp             | 914 ms                                                 | 496 ms: 1.84x faster                                                |
| richards                | 75.2 ms                                                | 43.6 ms: 1.72x faster                                               |
| pyflate                 | 676 ms                                                 | 395 ms: 1.71x faster                                                |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                |
| raytrace                | 467 ms                                                 | 281 ms: 1.66x faster                                                |
| scimark_monte_carlo     | 109 ms                                                 | 66.2 ms: 1.64x faster                                               |
| chaos                   | 106 ms                                                 | 65.9 ms: 1.60x faster                                               |
| hexiom                  | 9.43 ms                                                | 5.96 ms: 1.58x faster                                               |
| python_startup          | 14.1 ms                                                | 8.92 ms: 1.58x faster                                               |
| pickle_pure_python      | 452 us                                                 | 287 us: 1.58x faster                                                |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                |
| crypto_pyaes            | 117 ms                                                 | 76.5 ms: 1.53x faster                                               |
| spectral_norm           | 150 ms                                                 | 98.6 ms: 1.52x faster                                               |
| float                   | 109 ms                                                 | 71.9 ms: 1.51x faster                                               |
| nbody                   | 144 ms                                                 | 95.4 ms: 1.51x faster                                               |
| deepcopy_memo           | 51.7 us                                                | 34.5 us: 1.50x faster                                               |
| mako                    | 14.7 ms                                                | 9.81 ms: 1.49x faster                                               |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.49x faster                                               |
| chameleon               | 9.17 ms                                                | 6.28 ms: 1.46x faster                                               |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.46x faster                                                |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                               |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.42x faster                                              |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                               |
| html5lib                | 85.9 ms                                                | 60.5 ms: 1.42x faster                                               |
| json_dumps              | 13.4 ms                                                | 9.57 ms: 1.40x faster                                               |
| logging_simple          | 8.10 us                                                | 5.77 us: 1.40x faster                                               |
| django_template         | 46.3 ms                                                | 33.1 ms: 1.40x faster                                               |
| pprint_safe_repr        | 953 ms                                                 | 681 ms: 1.40x faster                                                |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                |
| scimark_fft             | 421 ms                                                 | 303 ms: 1.39x faster                                                |
| logging_format          | 8.85 us                                                | 6.41 us: 1.38x faster                                               |
| unpack_sequence         | 59.4 ns                                                | 43.3 ns: 1.37x faster                                               |
| thrift                  | 1.03 ms                                                | 758 us: 1.36x faster                                                |
| tornado_http            | 128 ms                                                 | 94.2 ms: 1.36x faster                                               |
| genshi_xml              | 63.7 ms                                                | 46.9 ms: 1.36x faster                                               |
| pycparser               | 1.53 sec                                               | 1.13 sec: 1.36x faster                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.02 ms: 1.36x faster                                               |
| async_tree_none         | 711 ms                                                 | 526 ms: 1.35x faster                                                |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                              |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 55.7 ms: 1.34x faster                                               |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                               |
| deepcopy                | 438 us                                                 | 330 us: 1.33x faster                                                |
| fannkuch                | 488 ms                                                 | 368 ms: 1.32x faster                                                |
| mypy2                   | 430 ms                                                 | 330 ms: 1.30x faster                                                |
| async_tree_memoization  | 855 ms                                                 | 659 ms: 1.30x faster                                                |
| deepcopy_reduce         | 3.79 us                                                | 2.93 us: 1.29x faster                                               |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                |
| sqlglot_optimize        | 65.2 ms                                                | 51.1 ms: 1.28x faster                                               |
| nqueens                 | 100 ms                                                 | 79.1 ms: 1.27x faster                                               |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                                |
| coroutines              | 31.6 ms                                                | 25.6 ms: 1.24x faster                                               |
| dulwich_log             | 75.8 ms                                                | 62.3 ms: 1.22x faster                                               |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.21x faster                                               |
| bench_thread_pool       | 946 us                                                 | 782 us: 1.21x faster                                                |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                                |
| json_loads              | 28.7 us                                                | 23.8 us: 1.21x faster                                               |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                                |
| regex_v8                | 25.0 ms                                                | 21.0 ms: 1.19x faster                                               |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.0 ms: 1.19x faster                                               |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                                |
| sympy_sum               | 183 ms                                                 | 157 ms: 1.16x faster                                                |
| xml_etree_generate      | 93.8 ms                                                | 80.8 ms: 1.16x faster                                               |
| pickle_list             | 4.72 us                                                | 4.09 us: 1.15x faster                                               |
| json                    | 5.35 ms                                                | 4.67 ms: 1.14x faster                                               |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.14x faster                                               |
| djangocms               | 36.9 us                                                | 32.7 us: 1.13x faster                                               |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                               |
| mdp                     | 2.74 sec                                               | 2.44 sec: 1.12x faster                                              |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.07x faster                                                |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                               |
| telco                   | 6.73 ms                                                | 6.42 ms: 1.05x faster                                               |
| generators              | 76.4 ms                                                | 75.4 ms: 1.01x faster                                               |
| unpickle_list           | 4.92 us                                                | 4.87 us: 1.01x faster                                               |
| async_generators        | 426 ms                                                 | 429 ms: 1.01x slower                                                |
| regex_dna               | 214 ms                                                 | 219 ms: 1.02x slower                                                |
| pidigits                | 190 ms                                                 | 203 ms: 1.07x slower                                                |
| regex_effbot            | 3.19 ms                                                | 3.43 ms: 1.07x slower                                               |
| pickle_dict             | 27.6 us                                                | 30.9 us: 1.12x slower                                               |
| python_startup_no_site  | 5.78 ms                                                | 6.48 ms: 1.12x slower                                               |
| coverage                | 74.7 ms                                                | 95.9 ms: 1.28x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (3): pickle, bench_mp_pool, gc_traversal
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, pylint
