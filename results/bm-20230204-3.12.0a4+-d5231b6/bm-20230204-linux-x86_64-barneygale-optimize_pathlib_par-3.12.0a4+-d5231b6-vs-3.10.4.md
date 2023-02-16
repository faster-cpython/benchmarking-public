
# Results vs. 3.10.4

- fork: barneygale
- ref: optimize_pathlib_par
- machine: linux-x86_64
- commit hash: d5231b6
- commit date: 2023-02-04
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                       |
| chameleon      | 9.17 ms                                                | 6.27 ms: 1.46x faster                                                      |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                     |
| html5lib       | 85.9 ms                                                | 60.4 ms: 1.42x faster                                                      |
| tornado_http   | 128 ms                                                 | 93.7 ms: 1.37x faster                                                      |
| Geometric mean | (ref)                                                  | 1.37x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 92.6 ms: 1.55x faster                                                      |
| float          | 109 ms                                                 | 72.2 ms: 1.51x faster                                                      |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.33x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                       |
| regex_v8       | 25.0 ms                                                | 22.6 ms: 1.11x faster                                                      |
| regex_dna      | 214 ms                                                 | 216 ms: 1.01x slower                                                       |
| regex_effbot   | 3.19 ms                                                | 3.59 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 280 us: 1.61x faster                                                       |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                       |
| json_dumps           | 13.4 ms                                                | 9.22 ms: 1.46x faster                                                      |
| xml_etree_process    | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                      |
| xml_etree_generate   | 93.8 ms                                                | 77.7 ms: 1.21x faster                                                      |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                                      |
| pickle_list          | 4.72 us                                                | 4.17 us: 1.13x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 146 ms: 1.12x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.08x faster                                                       |
| unpickle             | 14.2 us                                                | 13.5 us: 1.05x faster                                                      |
| pickle               | 10.2 us                                                | 10.1 us: 1.01x faster                                                      |
| unpickle_list        | 4.92 us                                                | 4.98 us: 1.01x slower                                                      |
| pickle_dict          | 27.6 us                                                | 30.6 us: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.91 ms: 1.58x faster                                                      |
| python_startup_no_site | 5.78 ms                                                | 6.44 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.74 ms: 1.50x faster                                                      |
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.48x faster                                                      |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                      |
| genshi_xml      | 63.7 ms                                                | 46.5 ms: 1.37x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.19 ms: 2.28x faster                                                      |
| logging_silent          | 176 ns                                                 | 94.0 ns: 1.88x faster                                                      |
| asyncio_tcp             | 914 ms                                                 | 489 ms: 1.87x faster                                                       |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                       |
| richards                | 75.2 ms                                                | 42.3 ms: 1.78x faster                                                      |
| pyflate                 | 676 ms                                                 | 397 ms: 1.70x faster                                                       |
| scimark_monte_carlo     | 109 ms                                                 | 65.1 ms: 1.67x faster                                                      |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                       |
| chaos                   | 106 ms                                                 | 63.6 ms: 1.66x faster                                                      |
| raytrace                | 467 ms                                                 | 281 ms: 1.66x faster                                                       |
| pickle_pure_python      | 452 us                                                 | 280 us: 1.61x faster                                                       |
| crypto_pyaes            | 117 ms                                                 | 73.4 ms: 1.59x faster                                                      |
| spectral_norm           | 150 ms                                                 | 94.5 ms: 1.58x faster                                                      |
| python_startup          | 14.1 ms                                                | 8.91 ms: 1.58x faster                                                      |
| hexiom                  | 9.43 ms                                                | 6.03 ms: 1.56x faster                                                      |
| nbody                   | 144 ms                                                 | 92.6 ms: 1.55x faster                                                      |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                       |
| float                   | 109 ms                                                 | 72.2 ms: 1.51x faster                                                      |
| mako                    | 14.7 ms                                                | 9.74 ms: 1.50x faster                                                      |
| deepcopy_memo           | 51.7 us                                                | 34.5 us: 1.50x faster                                                      |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.48x faster                                                      |
| chameleon               | 9.17 ms                                                | 6.27 ms: 1.46x faster                                                      |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.46x faster                                                       |
| json_dumps              | 13.4 ms                                                | 9.22 ms: 1.46x faster                                                      |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.45x faster                                                     |
| pprint_safe_repr        | 953 ms                                                 | 666 ms: 1.43x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.43 ms: 1.43x faster                                                      |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                      |
| html5lib                | 85.9 ms                                                | 60.4 ms: 1.42x faster                                                      |
| logging_simple          | 8.10 us                                                | 5.72 us: 1.42x faster                                                      |
| sqlglot_transpile       | 2.43 ms                                                | 1.72 ms: 1.41x faster                                                      |
| scimark_fft             | 421 ms                                                 | 302 ms: 1.39x faster                                                       |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                       |
| logging_format          | 8.85 us                                                | 6.36 us: 1.39x faster                                                      |
| xml_etree_process       | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                      |
| unpack_sequence         | 59.4 ns                                                | 43.1 ns: 1.38x faster                                                      |
| thrift                  | 1.03 ms                                                | 752 us: 1.38x faster                                                       |
| genshi_xml              | 63.7 ms                                                | 46.5 ms: 1.37x faster                                                      |
| tornado_http            | 128 ms                                                 | 93.7 ms: 1.37x faster                                                      |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.99 ms: 1.37x faster                                                      |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                                     |
| fannkuch                | 488 ms                                                 | 359 ms: 1.36x faster                                                       |
| async_tree_none         | 711 ms                                                 | 525 ms: 1.35x faster                                                       |
| aiohttp                 | 1.34 ms                                                | 995 us: 1.35x faster                                                       |
| deepcopy                | 438 us                                                 | 328 us: 1.33x faster                                                       |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                                      |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                                     |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                       |
| async_tree_memoization  | 855 ms                                                 | 654 ms: 1.31x faster                                                       |
| nqueens                 | 100 ms                                                 | 77.0 ms: 1.30x faster                                                      |
| deepcopy_reduce         | 3.79 us                                                | 2.93 us: 1.29x faster                                                      |
| sqlglot_optimize        | 65.2 ms                                                | 51.1 ms: 1.28x faster                                                      |
| coroutines              | 31.6 ms                                                | 24.8 ms: 1.28x faster                                                      |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.27x faster                                                       |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 757 ms: 1.25x faster                                                       |
| async_generators        | 426 ms                                                 | 350 ms: 1.22x faster                                                       |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.21x faster                                                      |
| dulwich_log             | 75.8 ms                                                | 62.8 ms: 1.21x faster                                                      |
| sympy_str               | 325 ms                                                 | 269 ms: 1.21x faster                                                       |
| xml_etree_generate      | 93.8 ms                                                | 77.7 ms: 1.21x faster                                                      |
| bench_thread_pool       | 946 us                                                 | 785 us: 1.21x faster                                                       |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                                      |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                       |
| sympy_expand            | 534 ms                                                 | 456 ms: 1.17x faster                                                       |
| json                    | 5.35 ms                                                | 4.63 ms: 1.15x faster                                                      |
| djangocms               | 36.9 us                                                | 32.1 us: 1.15x faster                                                      |
| pickle_list             | 4.72 us                                                | 4.17 us: 1.13x faster                                                      |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                                      |
| mdp                     | 2.74 sec                                               | 2.44 sec: 1.12x faster                                                     |
| sqlite_synth            | 2.92 us                                                | 2.61 us: 1.12x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 146 ms: 1.12x faster                                                       |
| regex_v8                | 25.0 ms                                                | 22.6 ms: 1.11x faster                                                      |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.08x faster                                                       |
| pathlib                 | 20.0 ms                                                | 19.0 ms: 1.05x faster                                                      |
| telco                   | 6.73 ms                                                | 6.41 ms: 1.05x faster                                                      |
| unpickle                | 14.2 us                                                | 13.5 us: 1.05x faster                                                      |
| generators              | 76.4 ms                                                | 74.2 ms: 1.03x faster                                                      |
| pickle                  | 10.2 us                                                | 10.1 us: 1.01x faster                                                      |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                       |
| regex_dna               | 214 ms                                                 | 216 ms: 1.01x slower                                                       |
| unpickle_list           | 4.92 us                                                | 4.98 us: 1.01x slower                                                      |
| pickle_dict             | 27.6 us                                                | 30.6 us: 1.11x slower                                                      |
| python_startup_no_site  | 5.78 ms                                                | 6.44 ms: 1.12x slower                                                      |
| regex_effbot            | 3.19 ms                                                | 3.59 ms: 1.12x slower                                                      |
| dask                    | 436 ms                                                 | 498 ms: 1.14x slower                                                       |
| coverage                | 74.7 ms                                                | 95.1 ms: 1.27x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                               |

Benchmark hidden because not significant (2): bench_mp_pool, gc_traversal
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230204-3.12.0a4+-d5231b6/bm-20230204-linux-x86_64-barneygale-optimize_pathlib_par-3.12.0a4+-d5231b6.json: mypy
