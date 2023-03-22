
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0
- machine: linux-x86_64
- commit hash: deaf509
- commit date: 2022-10-24
- overall geometric mean: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 259 ms: 1.29x faster                                   |
| chameleon      | 9.17 ms                                                | 6.38 ms: 1.44x faster                                  |
| docutils       | 3.18 sec                                               | 2.60 sec: 1.22x faster                                 |
| html5lib       | 85.9 ms                                                | 64.8 ms: 1.32x faster                                  |
| tornado_http   | 128 ms                                                 | 96.5 ms: 1.33x faster                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 90.0 ms: 1.60x faster                                  |
| float          | 109 ms                                                 | 76.8 ms: 1.42x faster                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| regex_dna      | 214 ms                                                 | 203 ms: 1.05x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.46 ms: 1.08x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 308 us: 1.47x faster                                   |
| xml_etree_process    | 74.5 ms                                                | 53.7 ms: 1.39x faster                                  |
| unpickle_pure_python | 302 us                                                 | 227 us: 1.33x faster                                   |
| xml_etree_generate   | 93.8 ms                                                | 75.9 ms: 1.24x faster                                  |
| pickle_list          | 4.72 us                                                | 4.14 us: 1.14x faster                                  |
| json_loads           | 28.7 us                                                | 26.1 us: 1.10x faster                                  |
| json_dumps           | 13.4 ms                                                | 12.4 ms: 1.09x faster                                  |
| unpickle             | 14.2 us                                                | 13.3 us: 1.07x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| pickle               | 10.2 us                                                | 9.90 us: 1.03x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 160 ms: 1.02x faster                                   |
| unpickle_list        | 4.92 us                                                | 4.99 us: 1.01x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.2 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.58 ms: 1.64x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.04 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.83 ms: 1.49x faster                                  |
| django_template | 46.3 ms                                                | 32.3 ms: 1.43x faster                                  |
| genshi_text     | 30.6 ms                                                | 21.5 ms: 1.42x faster                                  |
| genshi_xml      | 63.7 ms                                                | 51.4 ms: 1.24x faster                                  |
| Geometric mean  | (ref)                                                  | 1.39x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.66 ms: 1.99x faster                                  |
| logging_silent          | 176 ns                                                 | 98.0 ns: 1.80x faster                                  |
| scimark_sor             | 197 ms                                                 | 115 ms: 1.71x faster                                   |
| python_startup          | 14.1 ms                                                | 8.58 ms: 1.64x faster                                  |
| richards                | 75.2 ms                                                | 46.1 ms: 1.63x faster                                  |
| pyflate                 | 676 ms                                                 | 419 ms: 1.61x faster                                   |
| go                      | 226 ms                                                 | 140 ms: 1.61x faster                                   |
| raytrace                | 467 ms                                                 | 291 ms: 1.60x faster                                   |
| nbody                   | 144 ms                                                 | 90.0 ms: 1.60x faster                                  |
| scimark_monte_carlo     | 109 ms                                                 | 68.0 ms: 1.60x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 75.7 ms: 1.54x faster                                  |
| chaos                   | 106 ms                                                 | 68.7 ms: 1.54x faster                                  |
| spectral_norm           | 150 ms                                                 | 98.1 ms: 1.52x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.36 ms: 1.50x faster                                  |
| mako                    | 14.7 ms                                                | 9.83 ms: 1.49x faster                                  |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                   |
| hexiom                  | 9.43 ms                                                | 6.34 ms: 1.49x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.65 ms: 1.47x faster                                  |
| pickle_pure_python      | 452 us                                                 | 308 us: 1.47x faster                                   |
| deepcopy_memo           | 51.7 us                                                | 35.8 us: 1.44x faster                                  |
| chameleon               | 9.17 ms                                                | 6.38 ms: 1.44x faster                                  |
| django_template         | 46.3 ms                                                | 32.3 ms: 1.43x faster                                  |
| genshi_text             | 30.6 ms                                                | 21.5 ms: 1.42x faster                                  |
| float                   | 109 ms                                                 | 76.8 ms: 1.42x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 53.7 ms: 1.39x faster                                  |
| async_tree_memoization  | 855 ms                                                 | 624 ms: 1.37x faster                                   |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                 |
| logging_format          | 8.85 us                                                | 6.48 us: 1.37x faster                                  |
| thrift                  | 1.03 ms                                                | 760 us: 1.36x faster                                   |
| pprint_pformat          | 1.98 sec                                               | 1.46 sec: 1.36x faster                                 |
| async_tree_none         | 711 ms                                                 | 526 ms: 1.35x faster                                   |
| pprint_safe_repr        | 953 ms                                                 | 706 ms: 1.35x faster                                   |
| logging_simple          | 8.10 us                                                | 6.02 us: 1.35x faster                                  |
| unpack_sequence         | 59.4 ns                                                | 44.5 ns: 1.34x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 227 us: 1.33x faster                                   |
| tornado_http            | 128 ms                                                 | 96.5 ms: 1.33x faster                                  |
| html5lib                | 85.9 ms                                                | 64.8 ms: 1.32x faster                                  |
| regex_compile           | 177 ms                                                 | 136 ms: 1.30x faster                                   |
| scimark_fft             | 421 ms                                                 | 325 ms: 1.29x faster                                   |
| 2to3                    | 335 ms                                                 | 259 ms: 1.29x faster                                   |
| pycparser               | 1.53 sec                                               | 1.19 sec: 1.29x faster                                 |
| async_tree_cpu_io_mixed | 949 ms                                                 | 736 ms: 1.29x faster                                   |
| deepcopy                | 438 us                                                 | 341 us: 1.28x faster                                   |
| gunicorn                | 1.43 ms                                                | 1.12 ms: 1.28x faster                                  |
| aiohttp                 | 1.34 ms                                                | 1.05 ms: 1.28x faster                                  |
| fannkuch                | 488 ms                                                 | 384 ms: 1.27x faster                                   |
| deepcopy_reduce         | 3.79 us                                                | 3.02 us: 1.26x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 108 ms: 1.25x faster                                   |
| genshi_xml              | 63.7 ms                                                | 51.4 ms: 1.24x faster                                  |
| sqlglot_optimize        | 65.2 ms                                                | 52.7 ms: 1.24x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 75.9 ms: 1.24x faster                                  |
| docutils                | 3.18 sec                                               | 2.60 sec: 1.22x faster                                 |
| coroutines              | 31.6 ms                                                | 26.2 ms: 1.21x faster                                  |
| async_generators        | 426 ms                                                 | 356 ms: 1.20x faster                                   |
| nqueens                 | 100 ms                                                 | 83.8 ms: 1.19x faster                                  |
| dask                    | 436 ms                                                 | 365 ms: 1.19x faster                                   |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.19x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.59 ms: 1.19x faster                                  |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.1 ms: 1.19x faster                                  |
| dulwich_log             | 75.8 ms                                                | 64.0 ms: 1.19x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.48 us: 1.18x faster                                  |
| flaskblogging           | 8.27 ms                                                | 7.11 ms: 1.16x faster                                  |
| bench_thread_pool       | 946 us                                                 | 817 us: 1.16x faster                                   |
| pylint                  | 532 ms                                                 | 462 ms: 1.15x faster                                   |
| sympy_integrate         | 24.0 ms                                                | 21.0 ms: 1.15x faster                                  |
| pickle_list             | 4.72 us                                                | 4.14 us: 1.14x faster                                  |
| djangocms               | 36.9 us                                                | 32.5 us: 1.13x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| sympy_expand            | 534 ms                                                 | 475 ms: 1.12x faster                                   |
| sympy_str               | 325 ms                                                 | 291 ms: 1.12x faster                                   |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.11x faster                                  |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.11x faster                                   |
| json_loads              | 28.7 us                                                | 26.1 us: 1.10x faster                                  |
| json                    | 5.35 ms                                                | 4.87 ms: 1.10x faster                                  |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                   |
| create_gc_cycles        | 1.65 ms                                                | 1.52 ms: 1.09x faster                                  |
| json_dumps              | 13.4 ms                                                | 12.4 ms: 1.09x faster                                  |
| unpickle                | 14.2 us                                                | 13.3 us: 1.07x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| regex_dna               | 214 ms                                                 | 203 ms: 1.05x faster                                   |
| telco                   | 6.73 ms                                                | 6.43 ms: 1.05x faster                                  |
| mdp                     | 2.74 sec                                               | 2.63 sec: 1.04x faster                                 |
| generators              | 76.4 ms                                                | 73.5 ms: 1.04x faster                                  |
| asyncio_tcp             | 914 ms                                                 | 883 ms: 1.03x faster                                   |
| pickle                  | 10.2 us                                                | 9.90 us: 1.03x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 160 ms: 1.02x faster                                   |
| unpickle_list           | 4.92 us                                                | 4.99 us: 1.01x slower                                  |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| python_startup_no_site  | 5.78 ms                                                | 6.04 ms: 1.05x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.46 ms: 1.08x slower                                  |
| gc_traversal            | 3.53 ms                                                | 3.82 ms: 1.08x slower                                  |
| pickle_dict             | 27.6 us                                                | 31.2 us: 1.13x slower                                  |
| coverage                | 74.7 ms                                                | 99.3 ms: 1.33x slower                                  |
| Geometric mean          | (ref)                                                  | 1.25x faster                                           |

Benchmark hidden because not significant (2): mypy2, bench_mp_pool
