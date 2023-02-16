
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 666c084
- commit date: 2023-01-28
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                   |
| chameleon      | 9.17 ms                                                | 6.45 ms: 1.42x faster                                  |
| docutils       | 3.18 sec                                               | 2.48 sec: 1.28x faster                                 |
| html5lib       | 85.9 ms                                                | 60.1 ms: 1.43x faster                                  |
| tornado_http   | 128 ms                                                 | 94.4 ms: 1.36x faster                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 109 ms                                                 | 71.4 ms: 1.53x faster                                  |
| nbody          | 144 ms                                                 | 94.7 ms: 1.52x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.33x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                  |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.46 ms: 1.08x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 284 us: 1.59x faster                                   |
| unpickle_pure_python | 302 us                                                 | 201 us: 1.50x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.57 ms: 1.40x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 53.5 ms: 1.39x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 77.6 ms: 1.21x faster                                  |
| json_loads           | 28.7 us                                                | 24.1 us: 1.19x faster                                  |
| pickle_list          | 4.72 us                                                | 4.01 us: 1.18x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| unpickle             | 14.2 us                                                | 13.4 us: 1.05x faster                                  |
| pickle               | 10.2 us                                                | 10.3 us: 1.01x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.0 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.90 ms: 1.58x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.44 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.70 ms: 1.51x faster                                  |
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.49x faster                                  |
| django_template | 46.3 ms                                                | 32.8 ms: 1.41x faster                                  |
| genshi_xml      | 63.7 ms                                                | 47.1 ms: 1.35x faster                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.19 ms: 2.28x faster                                  |
| logging_silent          | 176 ns                                                 | 92.4 ns: 1.91x faster                                  |
| asyncio_tcp             | 914 ms                                                 | 494 ms: 1.85x faster                                   |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                   |
| richards                | 75.2 ms                                                | 42.7 ms: 1.76x faster                                  |
| pyflate                 | 676 ms                                                 | 399 ms: 1.69x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 65.5 ms: 1.66x faster                                  |
| raytrace                | 467 ms                                                 | 282 ms: 1.66x faster                                   |
| chaos                   | 106 ms                                                 | 64.8 ms: 1.63x faster                                  |
| go                      | 226 ms                                                 | 140 ms: 1.61x faster                                   |
| crypto_pyaes            | 117 ms                                                 | 72.9 ms: 1.60x faster                                  |
| pickle_pure_python      | 452 us                                                 | 284 us: 1.59x faster                                   |
| hexiom                  | 9.43 ms                                                | 5.94 ms: 1.59x faster                                  |
| python_startup          | 14.1 ms                                                | 8.90 ms: 1.58x faster                                  |
| spectral_norm           | 150 ms                                                 | 97.9 ms: 1.53x faster                                  |
| float                   | 109 ms                                                 | 71.4 ms: 1.53x faster                                  |
| nbody                   | 144 ms                                                 | 94.7 ms: 1.52x faster                                  |
| mako                    | 14.7 ms                                                | 9.70 ms: 1.51x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 201 us: 1.50x faster                                   |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                   |
| deepcopy_memo           | 51.7 us                                                | 34.7 us: 1.49x faster                                  |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.49x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.43x faster                                 |
| html5lib                | 85.9 ms                                                | 60.1 ms: 1.43x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.43x faster                                  |
| chameleon               | 9.17 ms                                                | 6.45 ms: 1.42x faster                                  |
| unpack_sequence         | 59.4 ns                                                | 41.9 ns: 1.42x faster                                  |
| django_template         | 46.3 ms                                                | 32.8 ms: 1.41x faster                                  |
| pprint_safe_repr        | 953 ms                                                 | 675 ms: 1.41x faster                                   |
| json_dumps              | 13.4 ms                                                | 9.57 ms: 1.40x faster                                  |
| logging_simple          | 8.10 us                                                | 5.79 us: 1.40x faster                                  |
| logging_format          | 8.85 us                                                | 6.35 us: 1.39x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 53.5 ms: 1.39x faster                                  |
| thrift                  | 1.03 ms                                                | 744 us: 1.39x faster                                   |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                 |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                   |
| scimark_fft             | 421 ms                                                 | 308 ms: 1.37x faster                                   |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                 |
| tornado_http            | 128 ms                                                 | 94.4 ms: 1.36x faster                                  |
| async_tree_none         | 711 ms                                                 | 525 ms: 1.35x faster                                   |
| genshi_xml              | 63.7 ms                                                | 47.1 ms: 1.35x faster                                  |
| fannkuch                | 488 ms                                                 | 361 ms: 1.35x faster                                   |
| aiohttp                 | 1.34 ms                                                | 998 us: 1.34x faster                                   |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                  |
| deepcopy                | 438 us                                                 | 327 us: 1.34x faster                                   |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.15 ms: 1.31x faster                                  |
| async_tree_memoization  | 855 ms                                                 | 656 ms: 1.30x faster                                   |
| nqueens                 | 100 ms                                                 | 78.1 ms: 1.28x faster                                  |
| docutils                | 3.18 sec                                               | 2.48 sec: 1.28x faster                                 |
| sqlglot_optimize        | 65.2 ms                                                | 51.0 ms: 1.28x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.27x faster                                   |
| coroutines              | 31.6 ms                                                | 24.9 ms: 1.27x faster                                  |
| deepcopy_reduce         | 3.79 us                                                | 3.00 us: 1.26x faster                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 758 ms: 1.25x faster                                   |
| async_generators        | 426 ms                                                 | 350 ms: 1.22x faster                                   |
| sympy_integrate         | 24.0 ms                                                | 19.9 ms: 1.21x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 77.6 ms: 1.21x faster                                  |
| dulwich_log             | 75.8 ms                                                | 62.9 ms: 1.21x faster                                  |
| bench_thread_pool       | 946 us                                                 | 786 us: 1.20x faster                                   |
| sympy_str               | 325 ms                                                 | 272 ms: 1.20x faster                                   |
| json_loads              | 28.7 us                                                | 24.1 us: 1.19x faster                                  |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                  |
| pickle_list             | 4.72 us                                                | 4.01 us: 1.18x faster                                  |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                   |
| djangocms               | 36.9 us                                                | 31.9 us: 1.16x faster                                  |
| json                    | 5.35 ms                                                | 4.66 ms: 1.15x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                  |
| create_gc_cycles        | 1.65 ms                                                | 1.45 ms: 1.13x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.13x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| unpickle                | 14.2 us                                                | 13.4 us: 1.05x faster                                  |
| telco                   | 6.73 ms                                                | 6.45 ms: 1.04x faster                                  |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                   |
| mdp                     | 2.74 sec                                               | 2.68 sec: 1.02x faster                                 |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| pickle                  | 10.2 us                                                | 10.3 us: 1.01x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.46 ms: 1.08x slower                                  |
| gc_traversal            | 3.53 ms                                                | 3.82 ms: 1.08x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.44 ms: 1.12x slower                                  |
| pickle_dict             | 27.6 us                                                | 31.0 us: 1.12x slower                                  |
| dask                    | 436 ms                                                 | 500 ms: 1.15x slower                                   |
| coverage                | 74.7 ms                                                | 98.3 ms: 1.31x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (3): bench_mp_pool, generators, unpickle_list
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230128-3.12.0a4+-666c084/bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084.json: mypy
