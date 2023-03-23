
# Results vs. 3.10.4

- fork: brandtbucher
- ref: type_cache_fixed
- machine: linux-x86_64
- commit hash: bde6bec
- commit date: 2023-03-23
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                     |
| chameleon      | 9.17 ms                                                | 6.55 ms: 1.40x faster                                                    |
| docutils       | 3.18 sec                                               | 2.56 sec: 1.24x faster                                                   |
| html5lib       | 85.9 ms                                                | 62.2 ms: 1.38x faster                                                    |
| tornado_http   | 128 ms                                                 | 92.7 ms: 1.38x faster                                                    |
| Geometric mean | (ref)                                                  | 1.35x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 90.2 ms: 1.60x faster                                                    |
| float          | 109 ms                                                 | 74.0 ms: 1.47x faster                                                    |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.33x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                     |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.12x faster                                                    |
| regex_dna      | 214 ms                                                 | 204 ms: 1.05x faster                                                     |
| regex_effbot   | 3.19 ms                                                | 3.57 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 287 us: 1.58x faster                                                     |
| unpickle_pure_python | 302 us                                                 | 201 us: 1.50x faster                                                     |
| json_dumps           | 13.4 ms                                                | 9.53 ms: 1.41x faster                                                    |
| xml_etree_process    | 74.5 ms                                                | 56.5 ms: 1.32x faster                                                    |
| json_loads           | 28.7 us                                                | 24.1 us: 1.19x faster                                                    |
| xml_etree_generate   | 93.8 ms                                                | 81.9 ms: 1.14x faster                                                    |
| pickle_list          | 4.72 us                                                | 4.24 us: 1.11x faster                                                    |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                     |
| pickle               | 10.2 us                                                | 10.5 us: 1.03x slower                                                    |
| unpickle_list        | 4.92 us                                                | 5.07 us: 1.03x slower                                                    |
| pickle_dict          | 27.6 us                                                | 31.9 us: 1.16x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.83 ms: 1.59x faster                                                    |
| python_startup_no_site | 5.78 ms                                                | 6.53 ms: 1.13x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.96 ms: 1.47x faster                                                    |
| genshi_text     | 30.6 ms                                                | 22.2 ms: 1.38x faster                                                    |
| django_template | 46.3 ms                                                | 33.8 ms: 1.37x faster                                                    |
| genshi_xml      | 63.7 ms                                                | 48.2 ms: 1.32x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.7 ms: 2.57x faster                                                    |
| deltablue               | 7.28 ms                                                | 3.40 ms: 2.14x faster                                                    |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.80x faster                                                     |
| asyncio_tcp             | 914 ms                                                 | 509 ms: 1.80x faster                                                     |
| logging_silent          | 176 ns                                                 | 98.4 ns: 1.79x faster                                                    |
| richards                | 75.2 ms                                                | 44.1 ms: 1.71x faster                                                    |
| raytrace                | 467 ms                                                 | 283 ms: 1.65x faster                                                     |
| go                      | 226 ms                                                 | 138 ms: 1.63x faster                                                     |
| pyflate                 | 676 ms                                                 | 419 ms: 1.61x faster                                                     |
| scimark_monte_carlo     | 109 ms                                                 | 67.6 ms: 1.60x faster                                                    |
| nbody                   | 144 ms                                                 | 90.2 ms: 1.60x faster                                                    |
| python_startup          | 14.1 ms                                                | 8.83 ms: 1.59x faster                                                    |
| spectral_norm           | 150 ms                                                 | 94.3 ms: 1.59x faster                                                    |
| pickle_pure_python      | 452 us                                                 | 287 us: 1.58x faster                                                     |
| chaos                   | 106 ms                                                 | 67.7 ms: 1.56x faster                                                    |
| crypto_pyaes            | 117 ms                                                 | 75.1 ms: 1.55x faster                                                    |
| hexiom                  | 9.43 ms                                                | 6.14 ms: 1.53x faster                                                    |
| deepcopy_memo           | 51.7 us                                                | 34.5 us: 1.50x faster                                                    |
| unpickle_pure_python    | 302 us                                                 | 201 us: 1.50x faster                                                     |
| float                   | 109 ms                                                 | 74.0 ms: 1.47x faster                                                    |
| mako                    | 14.7 ms                                                | 9.96 ms: 1.47x faster                                                    |
| scimark_lu              | 161 ms                                                 | 111 ms: 1.45x faster                                                     |
| unpack_sequence         | 59.4 ns                                                | 41.6 ns: 1.43x faster                                                    |
| json_dumps              | 13.4 ms                                                | 9.53 ms: 1.41x faster                                                    |
| pprint_pformat          | 1.98 sec                                               | 1.41 sec: 1.41x faster                                                   |
| chameleon               | 9.17 ms                                                | 6.55 ms: 1.40x faster                                                    |
| sqlglot_parse           | 2.04 ms                                                | 1.47 ms: 1.39x faster                                                    |
| logging_simple          | 8.10 us                                                | 5.83 us: 1.39x faster                                                    |
| logging_format          | 8.85 us                                                | 6.40 us: 1.38x faster                                                    |
| tornado_http            | 128 ms                                                 | 92.7 ms: 1.38x faster                                                    |
| pprint_safe_repr        | 953 ms                                                 | 690 ms: 1.38x faster                                                     |
| html5lib                | 85.9 ms                                                | 62.2 ms: 1.38x faster                                                    |
| genshi_text             | 30.6 ms                                                | 22.2 ms: 1.38x faster                                                    |
| sqlglot_transpile       | 2.43 ms                                                | 1.76 ms: 1.38x faster                                                    |
| coroutines              | 31.6 ms                                                | 23.0 ms: 1.38x faster                                                    |
| django_template         | 46.3 ms                                                | 33.8 ms: 1.37x faster                                                    |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                   |
| async_tree_none         | 711 ms                                                 | 531 ms: 1.34x faster                                                     |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                     |
| scimark_fft             | 421 ms                                                 | 317 ms: 1.33x faster                                                     |
| deepcopy                | 438 us                                                 | 330 us: 1.33x faster                                                     |
| genshi_xml              | 63.7 ms                                                | 48.2 ms: 1.32x faster                                                    |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                     |
| xml_etree_process       | 74.5 ms                                                | 56.5 ms: 1.32x faster                                                    |
| pycparser               | 1.53 sec                                               | 1.17 sec: 1.31x faster                                                   |
| gunicorn                | 1.43 ms                                                | 1.10 ms: 1.30x faster                                                    |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.24 ms: 1.29x faster                                                    |
| fannkuch                | 488 ms                                                 | 379 ms: 1.29x faster                                                     |
| thrift                  | 1.03 ms                                                | 806 us: 1.28x faster                                                     |
| mypy2                   | 430 ms                                                 | 337 ms: 1.27x faster                                                     |
| async_tree_memoization  | 855 ms                                                 | 673 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 748 ms: 1.27x faster                                                     |
| deepcopy_reduce         | 3.79 us                                                | 3.02 us: 1.26x faster                                                    |
| sqlglot_optimize        | 65.2 ms                                                | 52.0 ms: 1.25x faster                                                    |
| sqlglot_normalize       | 134 ms                                                 | 107 ms: 1.25x faster                                                     |
| docutils                | 3.18 sec                                               | 2.56 sec: 1.24x faster                                                   |
| nqueens                 | 100 ms                                                 | 81.9 ms: 1.22x faster                                                    |
| json_loads              | 28.7 us                                                | 24.1 us: 1.19x faster                                                    |
| bench_thread_pool       | 946 us                                                 | 796 us: 1.19x faster                                                     |
| dulwich_log             | 75.8 ms                                                | 64.1 ms: 1.18x faster                                                    |
| sympy_integrate         | 24.0 ms                                                | 20.6 ms: 1.17x faster                                                    |
| xml_etree_generate      | 93.8 ms                                                | 81.9 ms: 1.14x faster                                                    |
| json                    | 5.35 ms                                                | 4.67 ms: 1.14x faster                                                    |
| sympy_expand            | 534 ms                                                 | 467 ms: 1.14x faster                                                     |
| sympy_str               | 325 ms                                                 | 285 ms: 1.14x faster                                                     |
| djangocms               | 36.9 us                                                | 32.4 us: 1.14x faster                                                    |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                    |
| sqlite_synth            | 2.92 us                                                | 2.62 us: 1.12x faster                                                    |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.12x faster                                                    |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.12x faster                                                    |
| pickle_list             | 4.72 us                                                | 4.24 us: 1.11x faster                                                    |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                     |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                                     |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.10x faster                                                     |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                     |
| mdp                     | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                   |
| regex_dna               | 214 ms                                                 | 204 ms: 1.05x faster                                                     |
| telco                   | 6.73 ms                                                | 6.48 ms: 1.04x faster                                                    |
| async_generators        | 426 ms                                                 | 411 ms: 1.04x faster                                                     |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                     |
| gc_traversal            | 3.53 ms                                                | 3.54 ms: 1.00x slower                                                    |
| pickle                  | 10.2 us                                                | 10.5 us: 1.03x slower                                                    |
| unpickle_list           | 4.92 us                                                | 5.07 us: 1.03x slower                                                    |
| regex_effbot            | 3.19 ms                                                | 3.57 ms: 1.12x slower                                                    |
| python_startup_no_site  | 5.78 ms                                                | 6.53 ms: 1.13x slower                                                    |
| pickle_dict             | 27.6 us                                                | 31.9 us: 1.16x slower                                                    |
| dask                    | 436 ms                                                 | 512 ms: 1.17x slower                                                     |
| coverage                | 74.7 ms                                                | 96.3 ms: 1.29x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                             |

Benchmark hidden because not significant (2): unpickle, bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230323-3.12.0a6+-bde6bec/bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec.json: comprehensions
