
# Results vs. 3.10.4

- fork: brandtbucher
- ref: type_cache
- machine: linux-x86_64
- commit hash: 0e21f47
- commit date: 2023-03-23
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 253 ms: 1.32x faster                                               |
| chameleon      | 9.17 ms                                                | 6.63 ms: 1.38x faster                                              |
| docutils       | 3.18 sec                                               | 2.57 sec: 1.23x faster                                             |
| html5lib       | 85.9 ms                                                | 62.4 ms: 1.37x faster                                              |
| tornado_http   | 128 ms                                                 | 92.3 ms: 1.39x faster                                              |
| Geometric mean | (ref)                                                  | 1.34x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 86.8 ms: 1.66x faster                                              |
| float          | 109 ms                                                 | 73.7 ms: 1.48x faster                                              |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.33x faster                                               |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                              |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                               |
| regex_effbot   | 3.19 ms                                                | 3.57 ms: 1.12x slower                                              |
| Geometric mean | (ref)                                                  | 1.08x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 292 us: 1.55x faster                                               |
| unpickle_pure_python | 302 us                                                 | 200 us: 1.51x faster                                               |
| json_dumps           | 13.4 ms                                                | 9.71 ms: 1.38x faster                                              |
| xml_etree_process    | 74.5 ms                                                | 58.0 ms: 1.28x faster                                              |
| json_loads           | 28.7 us                                                | 24.2 us: 1.19x faster                                              |
| xml_etree_generate   | 93.8 ms                                                | 82.1 ms: 1.14x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 101 ms: 1.10x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                               |
| pickle_list          | 4.72 us                                                | 4.33 us: 1.09x faster                                              |
| pickle               | 10.2 us                                                | 10.4 us: 1.03x slower                                              |
| unpickle_list        | 4.92 us                                                | 5.28 us: 1.07x slower                                              |
| pickle_dict          | 27.6 us                                                | 30.7 us: 1.11x slower                                              |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                       |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.87 ms: 1.59x faster                                              |
| python_startup_no_site | 5.78 ms                                                | 6.55 ms: 1.13x slower                                              |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.0 ms: 1.46x faster                                              |
| genshi_text     | 30.6 ms                                                | 22.0 ms: 1.39x faster                                              |
| django_template | 46.3 ms                                                | 34.0 ms: 1.36x faster                                              |
| genshi_xml      | 63.7 ms                                                | 48.9 ms: 1.30x faster                                              |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.3 ms: 2.61x faster                                              |
| deltablue               | 7.28 ms                                                | 3.32 ms: 2.19x faster                                              |
| logging_silent          | 176 ns                                                 | 96.1 ns: 1.84x faster                                              |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                               |
| asyncio_tcp             | 914 ms                                                 | 509 ms: 1.80x faster                                               |
| richards                | 75.2 ms                                                | 43.9 ms: 1.71x faster                                              |
| nbody                   | 144 ms                                                 | 86.8 ms: 1.66x faster                                              |
| go                      | 226 ms                                                 | 137 ms: 1.64x faster                                               |
| scimark_monte_carlo     | 109 ms                                                 | 66.7 ms: 1.63x faster                                              |
| spectral_norm           | 150 ms                                                 | 93.6 ms: 1.60x faster                                              |
| raytrace                | 467 ms                                                 | 293 ms: 1.59x faster                                               |
| python_startup          | 14.1 ms                                                | 8.87 ms: 1.59x faster                                              |
| crypto_pyaes            | 117 ms                                                 | 73.7 ms: 1.58x faster                                              |
| chaos                   | 106 ms                                                 | 67.3 ms: 1.57x faster                                              |
| pyflate                 | 676 ms                                                 | 434 ms: 1.56x faster                                               |
| pickle_pure_python      | 452 us                                                 | 292 us: 1.55x faster                                               |
| hexiom                  | 9.43 ms                                                | 6.11 ms: 1.54x faster                                              |
| unpickle_pure_python    | 302 us                                                 | 200 us: 1.51x faster                                               |
| deepcopy_memo           | 51.7 us                                                | 34.4 us: 1.50x faster                                              |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                               |
| float                   | 109 ms                                                 | 73.7 ms: 1.48x faster                                              |
| mako                    | 14.7 ms                                                | 10.0 ms: 1.46x faster                                              |
| sqlglot_parse           | 2.04 ms                                                | 1.46 ms: 1.40x faster                                              |
| genshi_text             | 30.6 ms                                                | 22.0 ms: 1.39x faster                                              |
| coroutines              | 31.6 ms                                                | 22.7 ms: 1.39x faster                                              |
| tornado_http            | 128 ms                                                 | 92.3 ms: 1.39x faster                                              |
| pprint_pformat          | 1.98 sec                                               | 1.43 sec: 1.39x faster                                             |
| json_dumps              | 13.4 ms                                                | 9.71 ms: 1.38x faster                                              |
| sqlglot_transpile       | 2.43 ms                                                | 1.75 ms: 1.38x faster                                              |
| chameleon               | 9.17 ms                                                | 6.63 ms: 1.38x faster                                              |
| scimark_fft             | 421 ms                                                 | 306 ms: 1.38x faster                                               |
| html5lib                | 85.9 ms                                                | 62.4 ms: 1.37x faster                                              |
| logging_format          | 8.85 us                                                | 6.47 us: 1.37x faster                                              |
| pprint_safe_repr        | 953 ms                                                 | 698 ms: 1.36x faster                                               |
| logging_simple          | 8.10 us                                                | 5.95 us: 1.36x faster                                              |
| django_template         | 46.3 ms                                                | 34.0 ms: 1.36x faster                                              |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                             |
| async_tree_none         | 711 ms                                                 | 535 ms: 1.33x faster                                               |
| unpack_sequence         | 59.4 ns                                                | 44.7 ns: 1.33x faster                                              |
| regex_compile           | 177 ms                                                 | 134 ms: 1.33x faster                                               |
| 2to3                    | 335 ms                                                 | 253 ms: 1.32x faster                                               |
| deepcopy                | 438 us                                                 | 331 us: 1.32x faster                                               |
| genshi_xml              | 63.7 ms                                                | 48.9 ms: 1.30x faster                                              |
| pycparser               | 1.53 sec                                               | 1.18 sec: 1.30x faster                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.21 ms: 1.29x faster                                              |
| thrift                  | 1.03 ms                                                | 804 us: 1.29x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 58.0 ms: 1.28x faster                                              |
| mypy2                   | 430 ms                                                 | 337 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed | 949 ms                                                 | 750 ms: 1.27x faster                                               |
| async_tree_memoization  | 855 ms                                                 | 676 ms: 1.27x faster                                               |
| fannkuch                | 488 ms                                                 | 387 ms: 1.26x faster                                               |
| sqlglot_optimize        | 65.2 ms                                                | 52.2 ms: 1.25x faster                                              |
| deepcopy_reduce         | 3.79 us                                                | 3.05 us: 1.24x faster                                              |
| sqlglot_normalize       | 134 ms                                                 | 108 ms: 1.24x faster                                               |
| docutils                | 3.18 sec                                               | 2.57 sec: 1.23x faster                                             |
| nqueens                 | 100 ms                                                 | 81.2 ms: 1.23x faster                                              |
| json_loads              | 28.7 us                                                | 24.2 us: 1.19x faster                                              |
| bench_thread_pool       | 946 us                                                 | 799 us: 1.18x faster                                               |
| dulwich_log             | 75.8 ms                                                | 64.6 ms: 1.17x faster                                              |
| sympy_integrate         | 24.0 ms                                                | 20.6 ms: 1.17x faster                                              |
| json                    | 5.35 ms                                                | 4.68 ms: 1.14x faster                                              |
| xml_etree_generate      | 93.8 ms                                                | 82.1 ms: 1.14x faster                                              |
| sympy_expand            | 534 ms                                                 | 468 ms: 1.14x faster                                               |
| sympy_str               | 325 ms                                                 | 287 ms: 1.13x faster                                               |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                              |
| sqlite_synth            | 2.92 us                                                | 2.62 us: 1.12x faster                                              |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.11x faster                                              |
| xml_etree_iterparse     | 111 ms                                                 | 101 ms: 1.10x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                               |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                              |
| sympy_sum               | 183 ms                                                 | 167 ms: 1.10x faster                                               |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                               |
| pickle_list             | 4.72 us                                                | 4.33 us: 1.09x faster                                              |
| telco                   | 6.73 ms                                                | 6.40 ms: 1.05x faster                                              |
| mdp                     | 2.74 sec                                               | 2.64 sec: 1.04x faster                                             |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                               |
| async_generators        | 426 ms                                                 | 416 ms: 1.02x faster                                               |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                               |
| pickle                  | 10.2 us                                                | 10.4 us: 1.03x slower                                              |
| unpickle_list           | 4.92 us                                                | 5.28 us: 1.07x slower                                              |
| pickle_dict             | 27.6 us                                                | 30.7 us: 1.11x slower                                              |
| regex_effbot            | 3.19 ms                                                | 3.57 ms: 1.12x slower                                              |
| python_startup_no_site  | 5.78 ms                                                | 6.55 ms: 1.13x slower                                              |
| gc_traversal            | 3.53 ms                                                | 4.06 ms: 1.15x slower                                              |
| dask                    | 436 ms                                                 | 515 ms: 1.18x slower                                               |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                       |

Benchmark hidden because not significant (2): unpickle, bench_mp_pool
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, coverage, djangocms, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230323-3.12.0a6+-0e21f47/bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47.json: comprehensions
