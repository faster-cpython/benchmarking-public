
# Results vs. 3.10.4

- fork: iritkatriel
- ref: single_arg_exit
- machine: linux-x86_64
- commit hash: 00b5a0c
- commit date: 2023-01-27
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 254 ms: 1.32x faster                                                   |
| chameleon      | 9.17 ms                                                | 6.42 ms: 1.43x faster                                                  |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.26x faster                                                 |
| html5lib       | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                  |
| tornado_http   | 128 ms                                                 | 94.7 ms: 1.35x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.8 ms: 1.52x faster                                                  |
| float          | 109 ms                                                 | 72.5 ms: 1.50x faster                                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.38x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.5 ms: 1.17x faster                                                  |
| regex_dna      | 214 ms                                                 | 205 ms: 1.04x faster                                                   |
| regex_effbot   | 3.19 ms                                                | 3.37 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 285 us: 1.59x faster                                                   |
| unpickle_pure_python | 302 us                                                 | 201 us: 1.50x faster                                                   |
| json_dumps           | 13.4 ms                                                | 9.32 ms: 1.44x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                  |
| xml_etree_generate   | 93.8 ms                                                | 77.8 ms: 1.21x faster                                                  |
| pickle_list          | 4.72 us                                                | 4.15 us: 1.14x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 146 ms: 1.12x faster                                                   |
| json_loads           | 28.7 us                                                | 25.7 us: 1.12x faster                                                  |
| unpickle             | 14.2 us                                                | 13.0 us: 1.09x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.08x faster                                                   |
| unpickle_list        | 4.92 us                                                | 4.95 us: 1.01x slower                                                  |
| pickle_dict          | 27.6 us                                                | 31.3 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.96 ms: 1.57x faster                                                  |
| python_startup_no_site | 5.78 ms                                                | 6.54 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.45 ms: 1.55x faster                                                  |
| genshi_text     | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                  |
| django_template | 46.3 ms                                                | 33.3 ms: 1.39x faster                                                  |
| genshi_xml      | 63.7 ms                                                | 46.7 ms: 1.36x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.25 ms: 2.24x faster                                                  |
| logging_silent          | 176 ns                                                 | 92.0 ns: 1.92x faster                                                  |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                   |
| asyncio_tcp             | 914 ms                                                 | 498 ms: 1.83x faster                                                   |
| richards                | 75.2 ms                                                | 42.4 ms: 1.77x faster                                                  |
| pyflate                 | 676 ms                                                 | 394 ms: 1.71x faster                                                   |
| raytrace                | 467 ms                                                 | 283 ms: 1.65x faster                                                   |
| go                      | 226 ms                                                 | 138 ms: 1.63x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                 | 67.1 ms: 1.62x faster                                                  |
| crypto_pyaes            | 117 ms                                                 | 73.1 ms: 1.60x faster                                                  |
| pickle_pure_python      | 452 us                                                 | 285 us: 1.59x faster                                                   |
| hexiom                  | 9.43 ms                                                | 5.98 ms: 1.58x faster                                                  |
| python_startup          | 14.1 ms                                                | 8.96 ms: 1.57x faster                                                  |
| chaos                   | 106 ms                                                 | 67.2 ms: 1.57x faster                                                  |
| spectral_norm           | 150 ms                                                 | 95.4 ms: 1.57x faster                                                  |
| mako                    | 14.7 ms                                                | 9.45 ms: 1.55x faster                                                  |
| deepcopy_memo           | 51.7 us                                                | 33.8 us: 1.53x faster                                                  |
| nbody                   | 144 ms                                                 | 94.8 ms: 1.52x faster                                                  |
| float                   | 109 ms                                                 | 72.5 ms: 1.50x faster                                                  |
| unpickle_pure_python    | 302 us                                                 | 201 us: 1.50x faster                                                   |
| genshi_text             | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                                  |
| json_dumps              | 13.4 ms                                                | 9.32 ms: 1.44x faster                                                  |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.44x faster                                                 |
| scimark_lu              | 161 ms                                                 | 112 ms: 1.43x faster                                                   |
| chameleon               | 9.17 ms                                                | 6.42 ms: 1.43x faster                                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                                  |
| pprint_safe_repr        | 953 ms                                                 | 671 ms: 1.42x faster                                                   |
| html5lib                | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                  |
| xml_etree_process       | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                  |
| django_template         | 46.3 ms                                                | 33.3 ms: 1.39x faster                                                  |
| thrift                  | 1.03 ms                                                | 749 us: 1.38x faster                                                   |
| regex_compile           | 177 ms                                                 | 129 ms: 1.38x faster                                                   |
| logging_simple          | 8.10 us                                                | 5.87 us: 1.38x faster                                                  |
| async_tree_none         | 711 ms                                                 | 517 ms: 1.38x faster                                                   |
| logging_format          | 8.85 us                                                | 6.45 us: 1.37x faster                                                  |
| genshi_xml              | 63.7 ms                                                | 46.7 ms: 1.36x faster                                                  |
| pycparser               | 1.53 sec                                               | 1.12 sec: 1.36x faster                                                 |
| unpack_sequence         | 59.4 ns                                                | 43.8 ns: 1.36x faster                                                  |
| tornado_http            | 128 ms                                                 | 94.7 ms: 1.35x faster                                                  |
| scimark_fft             | 421 ms                                                 | 311 ms: 1.35x faster                                                   |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                 |
| deepcopy                | 438 us                                                 | 330 us: 1.33x faster                                                   |
| async_tree_memoization  | 855 ms                                                 | 646 ms: 1.32x faster                                                   |
| 2to3                    | 335 ms                                                 | 254 ms: 1.32x faster                                                   |
| aiohttp                 | 1.34 ms                                                | 1.02 ms: 1.31x faster                                                  |
| nqueens                 | 100 ms                                                 | 76.3 ms: 1.31x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.17 ms: 1.31x faster                                                  |
| deepcopy_reduce         | 3.79 us                                                | 2.92 us: 1.30x faster                                                  |
| gunicorn                | 1.43 ms                                                | 1.10 ms: 1.30x faster                                                  |
| fannkuch                | 488 ms                                                 | 381 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 747 ms: 1.27x faster                                                   |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.26x faster                                                 |
| coroutines              | 31.6 ms                                                | 25.2 ms: 1.26x faster                                                  |
| sqlglot_optimize        | 65.2 ms                                                | 52.1 ms: 1.25x faster                                                  |
| sqlglot_normalize       | 134 ms                                                 | 108 ms: 1.25x faster                                                   |
| async_generators        | 426 ms                                                 | 352 ms: 1.21x faster                                                   |
| dulwich_log             | 75.8 ms                                                | 62.7 ms: 1.21x faster                                                  |
| xml_etree_generate      | 93.8 ms                                                | 77.8 ms: 1.21x faster                                                  |
| sympy_integrate         | 24.0 ms                                                | 20.0 ms: 1.21x faster                                                  |
| sympy_str               | 325 ms                                                 | 273 ms: 1.19x faster                                                   |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                   |
| regex_v8                | 25.0 ms                                                | 21.5 ms: 1.17x faster                                                  |
| sympy_expand            | 534 ms                                                 | 461 ms: 1.16x faster                                                   |
| pickle_list             | 4.72 us                                                | 4.15 us: 1.14x faster                                                  |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                                  |
| json                    | 5.35 ms                                                | 4.78 ms: 1.12x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 146 ms: 1.12x faster                                                   |
| json_loads              | 28.7 us                                                | 25.7 us: 1.12x faster                                                  |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                  |
| mdp                     | 2.74 sec                                               | 2.47 sec: 1.11x faster                                                 |
| djangocms               | 36.9 us                                                | 33.5 us: 1.10x faster                                                  |
| unpickle                | 14.2 us                                                | 13.0 us: 1.09x faster                                                  |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.08x faster                                                   |
| telco                   | 6.73 ms                                                | 6.25 ms: 1.08x faster                                                  |
| regex_dna               | 214 ms                                                 | 205 ms: 1.04x faster                                                   |
| gc_traversal            | 3.53 ms                                                | 3.41 ms: 1.03x faster                                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| unpickle_list           | 4.92 us                                                | 4.95 us: 1.01x slower                                                  |
| create_gc_cycles        | 1.65 ms                                                | 1.66 ms: 1.01x slower                                                  |
| generators              | 76.4 ms                                                | 78.4 ms: 1.03x slower                                                  |
| regex_effbot            | 3.19 ms                                                | 3.37 ms: 1.06x slower                                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.54 ms: 1.13x slower                                                  |
| pickle_dict             | 27.6 us                                                | 31.3 us: 1.14x slower                                                  |
| dask                    | 436 ms                                                 | 518 ms: 1.19x slower                                                   |
| bench_mp_pool           | 24.0 ms                                                | 30.6 ms: 1.27x slower                                                  |
| coverage                | 74.7 ms                                                | 99.4 ms: 1.33x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                           |

Benchmark hidden because not significant (2): pickle, bench_thread_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230127-3.12.0a4+-00b5a0c/bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c.json: mypy
