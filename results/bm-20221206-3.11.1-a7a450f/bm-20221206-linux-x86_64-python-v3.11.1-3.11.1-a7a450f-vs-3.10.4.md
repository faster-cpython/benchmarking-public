
# Results vs. 3.10.4

- fork: python
- ref: v3.11.1
- machine: linux-x86_64
- commit hash: a7a450f
- commit date: 2022-12-06
- overall geometric mean: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 258 ms: 1.30x faster                                   |
| chameleon      | 9.17 ms                                                | 6.63 ms: 1.38x faster                                  |
| docutils       | 3.18 sec                                               | 2.57 sec: 1.24x faster                                 |
| html5lib       | 85.9 ms                                                | 63.4 ms: 1.35x faster                                  |
| tornado_http   | 128 ms                                                 | 99.8 ms: 1.28x faster                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 95.4 ms: 1.51x faster                                  |
| float          | 109 ms                                                 | 76.0 ms: 1.43x faster                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                  |
| regex_dna      | 214 ms                                                 | 200 ms: 1.07x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.31 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 310 us: 1.46x faster                                   |
| xml_etree_process    | 74.5 ms                                                | 53.7 ms: 1.39x faster                                  |
| unpickle_pure_python | 302 us                                                 | 229 us: 1.32x faster                                   |
| xml_etree_generate   | 93.8 ms                                                | 76.6 ms: 1.22x faster                                  |
| json_loads           | 28.7 us                                                | 24.0 us: 1.20x faster                                  |
| pickle_list          | 4.72 us                                                | 4.17 us: 1.13x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.07x faster                                   |
| json_dumps           | 13.4 ms                                                | 12.6 ms: 1.07x faster                                  |
| unpickle             | 14.2 us                                                | 13.4 us: 1.06x faster                                  |
| pickle               | 10.2 us                                                | 9.72 us: 1.05x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 158 ms: 1.03x faster                                   |
| unpickle_list        | 4.92 us                                                | 4.95 us: 1.01x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.1 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.49 ms: 1.66x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 5.98 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.92 ms: 1.48x faster                                  |
| django_template | 46.3 ms                                                | 33.2 ms: 1.39x faster                                  |
| genshi_text     | 30.6 ms                                                | 22.1 ms: 1.38x faster                                  |
| genshi_xml      | 63.7 ms                                                | 52.5 ms: 1.21x faster                                  |
| Geometric mean  | (ref)                                                  | 1.36x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.67 ms: 1.98x faster                                  |
| logging_silent          | 176 ns                                                 | 102 ns: 1.73x faster                                   |
| scimark_sor             | 197 ms                                                 | 116 ms: 1.70x faster                                   |
| python_startup          | 14.1 ms                                                | 8.49 ms: 1.66x faster                                  |
| pyflate                 | 676 ms                                                 | 415 ms: 1.63x faster                                   |
| go                      | 226 ms                                                 | 140 ms: 1.62x faster                                   |
| crypto_pyaes            | 117 ms                                                 | 72.6 ms: 1.61x faster                                  |
| richards                | 75.2 ms                                                | 46.9 ms: 1.60x faster                                  |
| raytrace                | 467 ms                                                 | 294 ms: 1.59x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 68.4 ms: 1.59x faster                                  |
| chaos                   | 106 ms                                                 | 69.6 ms: 1.52x faster                                  |
| nbody                   | 144 ms                                                 | 95.4 ms: 1.51x faster                                  |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.50x faster                                   |
| sqlglot_parse           | 2.04 ms                                                | 1.38 ms: 1.48x faster                                  |
| mako                    | 14.7 ms                                                | 9.92 ms: 1.48x faster                                  |
| spectral_norm           | 150 ms                                                 | 101 ms: 1.48x faster                                   |
| pickle_pure_python      | 452 us                                                 | 310 us: 1.46x faster                                   |
| hexiom                  | 9.43 ms                                                | 6.46 ms: 1.46x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.68 ms: 1.45x faster                                  |
| float                   | 109 ms                                                 | 76.0 ms: 1.43x faster                                  |
| django_template         | 46.3 ms                                                | 33.2 ms: 1.39x faster                                  |
| deepcopy_memo           | 51.7 us                                                | 37.2 us: 1.39x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 53.7 ms: 1.39x faster                                  |
| chameleon               | 9.17 ms                                                | 6.63 ms: 1.38x faster                                  |
| genshi_text             | 30.6 ms                                                | 22.1 ms: 1.38x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.44 sec: 1.38x faster                                 |
| async_tree_memoization  | 855 ms                                                 | 627 ms: 1.36x faster                                   |
| pprint_safe_repr        | 953 ms                                                 | 700 ms: 1.36x faster                                   |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                 |
| logging_simple          | 8.10 us                                                | 5.95 us: 1.36x faster                                  |
| async_tree_none         | 711 ms                                                 | 523 ms: 1.36x faster                                   |
| html5lib                | 85.9 ms                                                | 63.4 ms: 1.35x faster                                  |
| logging_format          | 8.85 us                                                | 6.54 us: 1.35x faster                                  |
| thrift                  | 1.03 ms                                                | 765 us: 1.35x faster                                   |
| unpack_sequence         | 59.4 ns                                                | 44.6 ns: 1.33x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 229 us: 1.32x faster                                   |
| pycparser               | 1.53 sec                                               | 1.16 sec: 1.31x faster                                 |
| 2to3                    | 335 ms                                                 | 258 ms: 1.30x faster                                   |
| regex_compile           | 177 ms                                                 | 137 ms: 1.29x faster                                   |
| scimark_fft             | 421 ms                                                 | 327 ms: 1.29x faster                                   |
| tornado_http            | 128 ms                                                 | 99.8 ms: 1.28x faster                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 742 ms: 1.28x faster                                   |
| aiohttp                 | 1.34 ms                                                | 1.05 ms: 1.28x faster                                  |
| gunicorn                | 1.43 ms                                                | 1.13 ms: 1.27x faster                                  |
| fannkuch                | 488 ms                                                 | 384 ms: 1.27x faster                                   |
| deepcopy                | 438 us                                                 | 349 us: 1.25x faster                                   |
| coroutines              | 31.6 ms                                                | 25.3 ms: 1.25x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 108 ms: 1.24x faster                                   |
| docutils                | 3.18 sec                                               | 2.57 sec: 1.24x faster                                 |
| deepcopy_reduce         | 3.79 us                                                | 3.09 us: 1.23x faster                                  |
| sqlglot_optimize        | 65.2 ms                                                | 53.3 ms: 1.22x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 76.6 ms: 1.22x faster                                  |
| genshi_xml              | 63.7 ms                                                | 52.5 ms: 1.21x faster                                  |
| json_loads              | 28.7 us                                                | 24.0 us: 1.20x faster                                  |
| dask                    | 436 ms                                                 | 365 ms: 1.20x faster                                   |
| dulwich_log             | 75.8 ms                                                | 63.5 ms: 1.19x faster                                  |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.0 ms: 1.19x faster                                  |
| async_generators        | 426 ms                                                 | 358 ms: 1.19x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.59 ms: 1.19x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.47 us: 1.18x faster                                  |
| nqueens                 | 100 ms                                                 | 85.0 ms: 1.18x faster                                  |
| flaskblogging           | 8.27 ms                                                | 7.07 ms: 1.17x faster                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 141 ms: 1.17x faster                                   |
| bench_thread_pool       | 946 us                                                 | 813 us: 1.16x faster                                   |
| json                    | 5.35 ms                                                | 4.63 ms: 1.16x faster                                  |
| pylint                  | 532 ms                                                 | 461 ms: 1.15x faster                                   |
| sympy_integrate         | 24.0 ms                                                | 21.0 ms: 1.15x faster                                  |
| pickle_list             | 4.72 us                                                | 4.17 us: 1.13x faster                                  |
| sympy_expand            | 534 ms                                                 | 472 ms: 1.13x faster                                   |
| sympy_str               | 325 ms                                                 | 289 ms: 1.12x faster                                   |
| regex_v8                | 25.0 ms                                                | 22.3 ms: 1.12x faster                                  |
| djangocms               | 36.9 us                                                | 33.1 us: 1.11x faster                                  |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.11x faster                                  |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.10x faster                                   |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.10x faster                                  |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.08x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.07x faster                                   |
| regex_dna               | 214 ms                                                 | 200 ms: 1.07x faster                                   |
| json_dumps              | 13.4 ms                                                | 12.6 ms: 1.07x faster                                  |
| unpickle                | 14.2 us                                                | 13.4 us: 1.06x faster                                  |
| pickle                  | 10.2 us                                                | 9.72 us: 1.05x faster                                  |
| generators              | 76.4 ms                                                | 73.3 ms: 1.04x faster                                  |
| mdp                     | 2.74 sec                                               | 2.64 sec: 1.04x faster                                 |
| xml_etree_parse         | 163 ms                                                 | 158 ms: 1.03x faster                                   |
| asyncio_tcp             | 914 ms                                                 | 889 ms: 1.03x faster                                   |
| telco                   | 6.73 ms                                                | 6.66 ms: 1.01x faster                                  |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| unpickle_list           | 4.92 us                                                | 4.95 us: 1.01x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 5.98 ms: 1.04x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.31 ms: 1.04x slower                                  |
| pickle_dict             | 27.6 us                                                | 31.1 us: 1.13x slower                                  |
| gc_traversal            | 3.53 ms                                                | 4.26 ms: 1.21x slower                                  |
| coverage                | 74.7 ms                                                | 104 ms: 1.39x slower                                   |
| Geometric mean          | (ref)                                                  | 1.25x faster                                           |

Benchmark hidden because not significant (2): mypy2, bench_mp_pool
