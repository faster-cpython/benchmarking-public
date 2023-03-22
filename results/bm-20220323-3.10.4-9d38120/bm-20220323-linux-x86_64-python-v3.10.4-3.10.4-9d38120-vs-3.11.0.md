
# Results vs. 3.11.0

- fork: python
- ref: v3.10.4
- machine: linux-x86_64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.25x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 335 ms: 1.29x slower                                   |
| chameleon      | 6.38 ms                                                | 9.17 ms: 1.44x slower                                  |
| docutils       | 2.60 sec                                               | 3.18 sec: 1.22x slower                                 |
| html5lib       | 64.8 ms                                                | 85.9 ms: 1.32x slower                                  |
| tornado_http   | 96.5 ms                                                | 128 ms: 1.33x slower                                   |
| Geometric mean | (ref)                                                  | 1.32x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                   |
| float          | 76.8 ms                                                | 109 ms: 1.42x slower                                   |
| nbody          | 90.0 ms                                                | 144 ms: 1.60x slower                                   |
| Geometric mean | (ref)                                                  | 1.30x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.19 ms: 1.08x faster                                  |
| regex_dna      | 203 ms                                                 | 214 ms: 1.05x slower                                   |
| regex_v8       | 22.2 ms                                                | 25.0 ms: 1.13x slower                                  |
| regex_compile  | 136 ms                                                 | 177 ms: 1.30x slower                                   |
| Geometric mean | (ref)                                                  | 1.09x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_dict          | 31.2 us                                                | 27.6 us: 1.13x faster                                  |
| unpickle_list        | 4.99 us                                                | 4.92 us: 1.01x faster                                  |
| xml_etree_parse      | 160 ms                                                 | 163 ms: 1.02x slower                                   |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                  |
| xml_etree_iterparse  | 104 ms                                                 | 111 ms: 1.07x slower                                   |
| unpickle             | 13.3 us                                                | 14.2 us: 1.07x slower                                  |
| json_dumps           | 12.4 ms                                                | 13.4 ms: 1.09x slower                                  |
| json_loads           | 26.1 us                                                | 28.7 us: 1.10x slower                                  |
| pickle_list          | 4.14 us                                                | 4.72 us: 1.14x slower                                  |
| xml_etree_generate   | 75.9 ms                                                | 93.8 ms: 1.24x slower                                  |
| unpickle_pure_python | 227 us                                                 | 302 us: 1.33x slower                                   |
| xml_etree_process    | 53.7 ms                                                | 74.5 ms: 1.39x slower                                  |
| pickle_pure_python   | 308 us                                                 | 452 us: 1.47x slower                                   |
| Geometric mean       | (ref)                                                  | 1.13x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 6.04 ms                                                | 5.78 ms: 1.05x faster                                  |
| python_startup         | 8.58 ms                                                | 14.1 ms: 1.64x slower                                  |
| Geometric mean         | (ref)                                                  | 1.25x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 63.7 ms: 1.24x slower                                  |
| genshi_text     | 21.5 ms                                                | 30.6 ms: 1.42x slower                                  |
| django_template | 32.3 ms                                                | 46.3 ms: 1.43x slower                                  |
| mako            | 9.83 ms                                                | 14.7 ms: 1.49x slower                                  |
| Geometric mean  | (ref)                                                  | 1.39x slower                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| coverage                | 99.3 ms                                                | 74.7 ms: 1.33x faster                                  |
| pickle_dict             | 31.2 us                                                | 27.6 us: 1.13x faster                                  |
| gc_traversal            | 3.82 ms                                                | 3.53 ms: 1.08x faster                                  |
| regex_effbot            | 3.46 ms                                                | 3.19 ms: 1.08x faster                                  |
| python_startup_no_site  | 6.04 ms                                                | 5.78 ms: 1.05x faster                                  |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                   |
| unpickle_list           | 4.99 us                                                | 4.92 us: 1.01x faster                                  |
| xml_etree_parse         | 160 ms                                                 | 163 ms: 1.02x slower                                   |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                  |
| asyncio_tcp             | 883 ms                                                 | 914 ms: 1.03x slower                                   |
| generators              | 73.5 ms                                                | 76.4 ms: 1.04x slower                                  |
| mdp                     | 2.63 sec                                               | 2.74 sec: 1.04x slower                                 |
| telco                   | 6.43 ms                                                | 6.73 ms: 1.05x slower                                  |
| regex_dna               | 203 ms                                                 | 214 ms: 1.05x slower                                   |
| xml_etree_iterparse     | 104 ms                                                 | 111 ms: 1.07x slower                                   |
| unpickle                | 13.3 us                                                | 14.2 us: 1.07x slower                                  |
| json_dumps              | 12.4 ms                                                | 13.4 ms: 1.09x slower                                  |
| create_gc_cycles        | 1.52 ms                                                | 1.65 ms: 1.09x slower                                  |
| meteor_contest          | 104 ms                                                 | 114 ms: 1.09x slower                                   |
| json                    | 4.87 ms                                                | 5.35 ms: 1.10x slower                                  |
| json_loads              | 26.1 us                                                | 28.7 us: 1.10x slower                                  |
| sympy_sum               | 166 ms                                                 | 183 ms: 1.11x slower                                   |
| pathlib                 | 18.1 ms                                                | 20.0 ms: 1.11x slower                                  |
| sympy_str               | 291 ms                                                 | 325 ms: 1.12x slower                                   |
| sympy_expand            | 475 ms                                                 | 534 ms: 1.12x slower                                   |
| regex_v8                | 22.2 ms                                                | 25.0 ms: 1.13x slower                                  |
| djangocms               | 32.5 us                                                | 36.9 us: 1.13x slower                                  |
| pickle_list             | 4.14 us                                                | 4.72 us: 1.14x slower                                  |
| sympy_integrate         | 21.0 ms                                                | 24.0 ms: 1.15x slower                                  |
| pylint                  | 462 ms                                                 | 532 ms: 1.15x slower                                   |
| bench_thread_pool       | 817 us                                                 | 946 us: 1.16x slower                                   |
| flaskblogging           | 7.11 ms                                                | 8.27 ms: 1.16x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.92 us: 1.18x slower                                  |
| dulwich_log             | 64.0 ms                                                | 75.8 ms: 1.19x slower                                  |
| sqlalchemy_imperative   | 18.1 ms                                                | 21.5 ms: 1.19x slower                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 5.45 ms: 1.19x slower                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 165 ms: 1.19x slower                                   |
| dask                    | 365 ms                                                 | 436 ms: 1.19x slower                                   |
| nqueens                 | 83.8 ms                                                | 100 ms: 1.19x slower                                   |
| async_generators        | 356 ms                                                 | 426 ms: 1.20x slower                                   |
| coroutines              | 26.2 ms                                                | 31.6 ms: 1.21x slower                                  |
| docutils                | 2.60 sec                                               | 3.18 sec: 1.22x slower                                 |
| xml_etree_generate      | 75.9 ms                                                | 93.8 ms: 1.24x slower                                  |
| sqlglot_optimize        | 52.7 ms                                                | 65.2 ms: 1.24x slower                                  |
| genshi_xml              | 51.4 ms                                                | 63.7 ms: 1.24x slower                                  |
| sqlglot_normalize       | 108 ms                                                 | 134 ms: 1.25x slower                                   |
| deepcopy_reduce         | 3.02 us                                                | 3.79 us: 1.26x slower                                  |
| fannkuch                | 384 ms                                                 | 488 ms: 1.27x slower                                   |
| aiohttp                 | 1.05 ms                                                | 1.34 ms: 1.28x slower                                  |
| gunicorn                | 1.12 ms                                                | 1.43 ms: 1.28x slower                                  |
| deepcopy                | 341 us                                                 | 438 us: 1.28x slower                                   |
| async_tree_cpu_io_mixed | 736 ms                                                 | 949 ms: 1.29x slower                                   |
| pycparser               | 1.19 sec                                               | 1.53 sec: 1.29x slower                                 |
| 2to3                    | 259 ms                                                 | 335 ms: 1.29x slower                                   |
| scimark_fft             | 325 ms                                                 | 421 ms: 1.29x slower                                   |
| regex_compile           | 136 ms                                                 | 177 ms: 1.30x slower                                   |
| html5lib                | 64.8 ms                                                | 85.9 ms: 1.32x slower                                  |
| tornado_http            | 96.5 ms                                                | 128 ms: 1.33x slower                                   |
| unpickle_pure_python    | 227 us                                                 | 302 us: 1.33x slower                                   |
| unpack_sequence         | 44.5 ns                                                | 59.4 ns: 1.34x slower                                  |
| logging_simple          | 6.02 us                                                | 8.10 us: 1.35x slower                                  |
| pprint_safe_repr        | 706 ms                                                 | 953 ms: 1.35x slower                                   |
| async_tree_none         | 526 ms                                                 | 711 ms: 1.35x slower                                   |
| pprint_pformat          | 1.46 sec                                               | 1.98 sec: 1.36x slower                                 |
| thrift                  | 760 us                                                 | 1.03 ms: 1.36x slower                                  |
| logging_format          | 6.48 us                                                | 8.85 us: 1.37x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.78 sec: 1.37x slower                                 |
| async_tree_memoization  | 624 ms                                                 | 855 ms: 1.37x slower                                   |
| xml_etree_process       | 53.7 ms                                                | 74.5 ms: 1.39x slower                                  |
| float                   | 76.8 ms                                                | 109 ms: 1.42x slower                                   |
| genshi_text             | 21.5 ms                                                | 30.6 ms: 1.42x slower                                  |
| django_template         | 32.3 ms                                                | 46.3 ms: 1.43x slower                                  |
| chameleon               | 6.38 ms                                                | 9.17 ms: 1.44x slower                                  |
| deepcopy_memo           | 35.8 us                                                | 51.7 us: 1.44x slower                                  |
| pickle_pure_python      | 308 us                                                 | 452 us: 1.47x slower                                   |
| sqlglot_transpile       | 1.65 ms                                                | 2.43 ms: 1.47x slower                                  |
| hexiom                  | 6.34 ms                                                | 9.43 ms: 1.49x slower                                  |
| scimark_lu              | 108 ms                                                 | 161 ms: 1.49x slower                                   |
| mako                    | 9.83 ms                                                | 14.7 ms: 1.49x slower                                  |
| sqlglot_parse           | 1.36 ms                                                | 2.04 ms: 1.50x slower                                  |
| spectral_norm           | 98.1 ms                                                | 150 ms: 1.52x slower                                   |
| chaos                   | 68.7 ms                                                | 106 ms: 1.54x slower                                   |
| crypto_pyaes            | 75.7 ms                                                | 117 ms: 1.54x slower                                   |
| scimark_monte_carlo     | 68.0 ms                                                | 109 ms: 1.60x slower                                   |
| nbody                   | 90.0 ms                                                | 144 ms: 1.60x slower                                   |
| raytrace                | 291 ms                                                 | 467 ms: 1.60x slower                                   |
| go                      | 140 ms                                                 | 226 ms: 1.61x slower                                   |
| pyflate                 | 419 ms                                                 | 676 ms: 1.61x slower                                   |
| richards                | 46.1 ms                                                | 75.2 ms: 1.63x slower                                  |
| python_startup          | 8.58 ms                                                | 14.1 ms: 1.64x slower                                  |
| scimark_sor             | 115 ms                                                 | 197 ms: 1.71x slower                                   |
| logging_silent          | 98.0 ns                                                | 176 ns: 1.80x slower                                   |
| deltablue               | 3.66 ms                                                | 7.28 ms: 1.99x slower                                  |
| Geometric mean          | (ref)                                                  | 1.25x slower                                           |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
