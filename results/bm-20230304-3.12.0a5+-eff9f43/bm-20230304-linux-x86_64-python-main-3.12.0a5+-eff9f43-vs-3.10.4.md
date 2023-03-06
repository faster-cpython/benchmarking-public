
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: eff9f43
- commit date: 2023-03-04
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 250 ms: 1.34x faster                                   |
| chameleon      | 9.17 ms                                                | 6.42 ms: 1.43x faster                                  |
| docutils       | 3.18 sec                                               | 2.56 sec: 1.24x faster                                 |
| html5lib       | 85.9 ms                                                | 61.4 ms: 1.40x faster                                  |
| tornado_http   | 128 ms                                                 | 94.9 ms: 1.35x faster                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.0 ms: 1.53x faster                                  |
| float          | 109 ms                                                 | 74.6 ms: 1.46x faster                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                  |
| regex_dna      | 214 ms                                                 | 209 ms: 1.02x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.40 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 291 us: 1.55x faster                                   |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.52x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.56 ms: 1.41x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 55.4 ms: 1.34x faster                                  |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                  |
| pickle_list          | 4.72 us                                                | 4.05 us: 1.17x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 81.3 ms: 1.15x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| unpickle             | 14.2 us                                                | 13.7 us: 1.03x faster                                  |
| unpickle_list        | 4.92 us                                                | 5.22 us: 1.06x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.5 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.03 ms: 1.56x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.55 ms: 1.13x slower                                  |
| Geometric mean         | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.1 ms: 1.45x faster                                  |
| genshi_text     | 30.6 ms                                                | 21.2 ms: 1.44x faster                                  |
| django_template | 46.3 ms                                                | 33.2 ms: 1.40x faster                                  |
| genshi_xml      | 63.7 ms                                                | 48.6 ms: 1.31x faster                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.6 ms: 2.50x faster                                  |
| deltablue               | 7.28 ms                                                | 3.20 ms: 2.28x faster                                  |
| logging_silent          | 176 ns                                                 | 93.2 ns: 1.89x faster                                  |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.81x faster                                   |
| asyncio_tcp             | 914 ms                                                 | 508 ms: 1.80x faster                                   |
| richards                | 75.2 ms                                                | 42.6 ms: 1.77x faster                                  |
| go                      | 226 ms                                                 | 133 ms: 1.70x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 68.0 ms: 1.60x faster                                  |
| pyflate                 | 676 ms                                                 | 424 ms: 1.59x faster                                   |
| raytrace                | 467 ms                                                 | 298 ms: 1.57x faster                                   |
| python_startup          | 14.1 ms                                                | 9.03 ms: 1.56x faster                                  |
| pickle_pure_python      | 452 us                                                 | 291 us: 1.55x faster                                   |
| chaos                   | 106 ms                                                 | 68.1 ms: 1.55x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 75.2 ms: 1.55x faster                                  |
| spectral_norm           | 150 ms                                                 | 97.3 ms: 1.54x faster                                  |
| nbody                   | 144 ms                                                 | 94.0 ms: 1.53x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.18 ms: 1.52x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.52x faster                                   |
| deepcopy_memo           | 51.7 us                                                | 34.4 us: 1.50x faster                                  |
| float                   | 109 ms                                                 | 74.6 ms: 1.46x faster                                  |
| mako                    | 14.7 ms                                                | 10.1 ms: 1.45x faster                                  |
| genshi_text             | 30.6 ms                                                | 21.2 ms: 1.44x faster                                  |
| scimark_lu              | 161 ms                                                 | 112 ms: 1.43x faster                                   |
| chameleon               | 9.17 ms                                                | 6.42 ms: 1.43x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.45 ms: 1.41x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.41 sec: 1.41x faster                                 |
| json_dumps              | 13.4 ms                                                | 9.56 ms: 1.41x faster                                  |
| html5lib                | 85.9 ms                                                | 61.4 ms: 1.40x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.74 ms: 1.40x faster                                  |
| django_template         | 46.3 ms                                                | 33.2 ms: 1.40x faster                                  |
| logging_simple          | 8.10 us                                                | 5.83 us: 1.39x faster                                  |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                 |
| pprint_safe_repr        | 953 ms                                                 | 687 ms: 1.39x faster                                   |
| unpack_sequence         | 59.4 ns                                                | 43.2 ns: 1.37x faster                                  |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                 |
| logging_format          | 8.85 us                                                | 6.48 us: 1.37x faster                                  |
| async_tree_none         | 711 ms                                                 | 522 ms: 1.36x faster                                   |
| tornado_http            | 128 ms                                                 | 94.9 ms: 1.35x faster                                  |
| coroutines              | 31.6 ms                                                | 23.5 ms: 1.35x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 55.4 ms: 1.34x faster                                  |
| 2to3                    | 335 ms                                                 | 250 ms: 1.34x faster                                   |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                   |
| thrift                  | 1.03 ms                                                | 777 us: 1.33x faster                                   |
| deepcopy                | 438 us                                                 | 329 us: 1.33x faster                                   |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                  |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.32x faster                                  |
| fannkuch                | 488 ms                                                 | 371 ms: 1.32x faster                                   |
| genshi_xml              | 63.7 ms                                                | 48.6 ms: 1.31x faster                                  |
| async_tree_memoization  | 855 ms                                                 | 653 ms: 1.31x faster                                   |
| scimark_fft             | 421 ms                                                 | 322 ms: 1.31x faster                                   |
| mypy2                   | 430 ms                                                 | 334 ms: 1.29x faster                                   |
| deepcopy_reduce         | 3.79 us                                                | 2.94 us: 1.29x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 745 ms: 1.27x faster                                   |
| sqlglot_optimize        | 65.2 ms                                                | 51.3 ms: 1.27x faster                                  |
| docutils                | 3.18 sec                                               | 2.56 sec: 1.24x faster                                 |
| nqueens                 | 100 ms                                                 | 82.2 ms: 1.22x faster                                  |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                  |
| dulwich_log             | 75.8 ms                                                | 63.2 ms: 1.20x faster                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                   |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.0 ms: 1.19x faster                                  |
| bench_thread_pool       | 946 us                                                 | 794 us: 1.19x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.60 ms: 1.19x faster                                  |
| pickle_list             | 4.72 us                                                | 4.05 us: 1.17x faster                                  |
| json                    | 5.35 ms                                                | 4.59 ms: 1.16x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.7 ms: 1.16x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 81.3 ms: 1.15x faster                                  |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                  |
| sympy_expand            | 534 ms                                                 | 466 ms: 1.14x faster                                   |
| djangocms               | 36.9 us                                                | 32.5 us: 1.14x faster                                  |
| sympy_str               | 325 ms                                                 | 288 ms: 1.13x faster                                   |
| sqlite_synth            | 2.92 us                                                | 2.63 us: 1.11x faster                                  |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                  |
| mdp                     | 2.74 sec                                               | 2.49 sec: 1.10x faster                                 |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| create_gc_cycles        | 1.65 ms                                                | 1.50 ms: 1.10x faster                                  |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                   |
| sympy_sum               | 183 ms                                                 | 168 ms: 1.09x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| unpickle                | 14.2 us                                                | 13.7 us: 1.03x faster                                  |
| regex_dna               | 214 ms                                                 | 209 ms: 1.02x faster                                   |
| telco                   | 6.73 ms                                                | 6.62 ms: 1.02x faster                                  |
| async_generators        | 426 ms                                                 | 421 ms: 1.01x faster                                   |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| unpickle_list           | 4.92 us                                                | 5.22 us: 1.06x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.40 ms: 1.06x slower                                  |
| gc_traversal            | 3.53 ms                                                | 3.84 ms: 1.09x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.55 ms: 1.13x slower                                  |
| pickle_dict             | 27.6 us                                                | 31.5 us: 1.14x slower                                  |
| dask                    | 436 ms                                                 | 507 ms: 1.16x slower                                   |
| coverage                | 74.7 ms                                                | 98.3 ms: 1.31x slower                                  |
| Geometric mean          | (ref)                                                  | 1.29x faster                                           |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230304-3.12.0a5+-eff9f43/bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43.json: comprehensions
