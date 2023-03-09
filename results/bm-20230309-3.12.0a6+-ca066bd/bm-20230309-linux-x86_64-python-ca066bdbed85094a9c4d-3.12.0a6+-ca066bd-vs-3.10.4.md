
# Results vs. 3.10.4

- fork: python
- ref: ca066bdbed85094a9c4d
- machine: linux-x86_64
- commit hash: ca066bd
- commit date: 2023-03-09
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                   |
| chameleon      | 9.17 ms                                                | 6.36 ms: 1.44x faster                                                  |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.24x faster                                                 |
| html5lib       | 85.9 ms                                                | 62.1 ms: 1.38x faster                                                  |
| tornado_http   | 128 ms                                                 | 95.1 ms: 1.35x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.1 ms: 1.55x faster                                                  |
| float          | 109 ms                                                 | 74.3 ms: 1.47x faster                                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.32x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.15x faster                                                  |
| regex_dna      | 214 ms                                                 | 205 ms: 1.04x faster                                                   |
| regex_effbot   | 3.19 ms                                                | 3.56 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 286 us: 1.58x faster                                                   |
| unpickle_pure_python | 302 us                                                 | 204 us: 1.48x faster                                                   |
| json_dumps           | 13.4 ms                                                | 9.62 ms: 1.40x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 55.7 ms: 1.34x faster                                                  |
| json_loads           | 28.7 us                                                | 24.4 us: 1.18x faster                                                  |
| xml_etree_generate   | 93.8 ms                                                | 80.9 ms: 1.16x faster                                                  |
| pickle_list          | 4.72 us                                                | 4.16 us: 1.14x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 101 ms: 1.10x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                   |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                                  |
| unpickle_list        | 4.92 us                                                | 4.97 us: 1.01x slower                                                  |
| pickle               | 10.2 us                                                | 10.5 us: 1.03x slower                                                  |
| pickle_dict          | 27.6 us                                                | 31.0 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.01 ms: 1.56x faster                                                  |
| python_startup_no_site | 5.78 ms                                                | 6.54 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.95 ms: 1.47x faster                                                  |
| genshi_text     | 30.6 ms                                                | 21.5 ms: 1.43x faster                                                  |
| django_template | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                  |
| genshi_xml      | 63.7 ms                                                | 48.0 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.6 ms: 2.50x faster                                                  |
| deltablue               | 7.28 ms                                                | 3.27 ms: 2.22x faster                                                  |
| logging_silent          | 176 ns                                                 | 93.6 ns: 1.88x faster                                                  |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.83x faster                                                   |
| asyncio_tcp             | 914 ms                                                 | 507 ms: 1.80x faster                                                   |
| richards                | 75.2 ms                                                | 43.6 ms: 1.72x faster                                                  |
| pyflate                 | 676 ms                                                 | 407 ms: 1.66x faster                                                   |
| raytrace                | 467 ms                                                 | 288 ms: 1.62x faster                                                   |
| go                      | 226 ms                                                 | 140 ms: 1.62x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                 | 68.3 ms: 1.59x faster                                                  |
| spectral_norm           | 150 ms                                                 | 94.3 ms: 1.59x faster                                                  |
| pickle_pure_python      | 452 us                                                 | 286 us: 1.58x faster                                                   |
| crypto_pyaes            | 117 ms                                                 | 74.2 ms: 1.57x faster                                                  |
| python_startup          | 14.1 ms                                                | 9.01 ms: 1.56x faster                                                  |
| nbody                   | 144 ms                                                 | 93.1 ms: 1.55x faster                                                  |
| chaos                   | 106 ms                                                 | 68.7 ms: 1.54x faster                                                  |
| hexiom                  | 9.43 ms                                                | 6.26 ms: 1.51x faster                                                  |
| unpickle_pure_python    | 302 us                                                 | 204 us: 1.48x faster                                                   |
| deepcopy_memo           | 51.7 us                                                | 35.0 us: 1.48x faster                                                  |
| mako                    | 14.7 ms                                                | 9.95 ms: 1.47x faster                                                  |
| float                   | 109 ms                                                 | 74.3 ms: 1.47x faster                                                  |
| chameleon               | 9.17 ms                                                | 6.36 ms: 1.44x faster                                                  |
| genshi_text             | 30.6 ms                                                | 21.5 ms: 1.43x faster                                                  |
| scimark_lu              | 161 ms                                                 | 113 ms: 1.42x faster                                                   |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                                 |
| sqlglot_parse           | 2.04 ms                                                | 1.44 ms: 1.42x faster                                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.73 ms: 1.40x faster                                                  |
| django_template         | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                  |
| json_dumps              | 13.4 ms                                                | 9.62 ms: 1.40x faster                                                  |
| pprint_safe_repr        | 953 ms                                                 | 686 ms: 1.39x faster                                                   |
| html5lib                | 85.9 ms                                                | 62.1 ms: 1.38x faster                                                  |
| unpack_sequence         | 59.4 ns                                                | 43.0 ns: 1.38x faster                                                  |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                                 |
| scimark_fft             | 421 ms                                                 | 309 ms: 1.36x faster                                                   |
| fannkuch                | 488 ms                                                 | 359 ms: 1.36x faster                                                   |
| logging_simple          | 8.10 us                                                | 5.96 us: 1.36x faster                                                  |
| async_tree_none         | 711 ms                                                 | 524 ms: 1.36x faster                                                   |
| pycparser               | 1.53 sec                                               | 1.13 sec: 1.35x faster                                                 |
| logging_format          | 8.85 us                                                | 6.56 us: 1.35x faster                                                  |
| tornado_http            | 128 ms                                                 | 95.1 ms: 1.35x faster                                                  |
| coroutines              | 31.6 ms                                                | 23.5 ms: 1.35x faster                                                  |
| xml_etree_process       | 74.5 ms                                                | 55.7 ms: 1.34x faster                                                  |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                  |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                   |
| thrift                  | 1.03 ms                                                | 778 us: 1.33x faster                                                   |
| genshi_xml              | 63.7 ms                                                | 48.0 ms: 1.33x faster                                                  |
| regex_compile           | 177 ms                                                 | 135 ms: 1.32x faster                                                   |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                  |
| async_tree_memoization  | 855 ms                                                 | 657 ms: 1.30x faster                                                   |
| deepcopy                | 438 us                                                 | 337 us: 1.30x faster                                                   |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.30x faster                                                   |
| mypy2                   | 430 ms                                                 | 335 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 741 ms: 1.28x faster                                                   |
| sqlglot_optimize        | 65.2 ms                                                | 51.0 ms: 1.28x faster                                                  |
| deepcopy_reduce         | 3.79 us                                                | 3.01 us: 1.26x faster                                                  |
| nqueens                 | 100 ms                                                 | 80.2 ms: 1.25x faster                                                  |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.24x faster                                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.55 ms: 1.20x faster                                                  |
| bench_thread_pool       | 946 us                                                 | 791 us: 1.20x faster                                                   |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.0 ms: 1.19x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 139 ms: 1.19x faster                                                   |
| dulwich_log             | 75.8 ms                                                | 63.7 ms: 1.19x faster                                                  |
| json_loads              | 28.7 us                                                | 24.4 us: 1.18x faster                                                  |
| sympy_integrate         | 24.0 ms                                                | 20.6 ms: 1.17x faster                                                  |
| xml_etree_generate      | 93.8 ms                                                | 80.9 ms: 1.16x faster                                                  |
| sympy_expand            | 534 ms                                                 | 462 ms: 1.15x faster                                                   |
| json                    | 5.35 ms                                                | 4.63 ms: 1.15x faster                                                  |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.15x faster                                                  |
| djangocms               | 36.9 us                                                | 32.3 us: 1.14x faster                                                  |
| pickle_list             | 4.72 us                                                | 4.16 us: 1.14x faster                                                  |
| sympy_str               | 325 ms                                                 | 287 ms: 1.13x faster                                                   |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                  |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.11x faster                                                  |
| sqlite_synth            | 2.92 us                                                | 2.63 us: 1.11x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 101 ms: 1.10x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                   |
| sympy_sum               | 183 ms                                                 | 167 ms: 1.10x faster                                                   |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                   |
| mdp                     | 2.74 sec                                               | 2.55 sec: 1.07x faster                                                 |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                                  |
| regex_dna               | 214 ms                                                 | 205 ms: 1.04x faster                                                   |
| telco                   | 6.73 ms                                                | 6.50 ms: 1.04x faster                                                  |
| async_generators        | 426 ms                                                 | 413 ms: 1.03x faster                                                   |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| gc_traversal            | 3.53 ms                                                | 3.55 ms: 1.01x slower                                                  |
| unpickle_list           | 4.92 us                                                | 4.97 us: 1.01x slower                                                  |
| pickle                  | 10.2 us                                                | 10.5 us: 1.03x slower                                                  |
| regex_effbot            | 3.19 ms                                                | 3.56 ms: 1.11x slower                                                  |
| pickle_dict             | 27.6 us                                                | 31.0 us: 1.12x slower                                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.54 ms: 1.13x slower                                                  |
| dask                    | 436 ms                                                 | 509 ms: 1.17x slower                                                   |
| coverage                | 74.7 ms                                                | 94.5 ms: 1.26x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230309-3.12.0a6+-ca066bd/bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd.json: comprehensions
