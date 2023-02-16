
# Results vs. 3.10.4

- fork: gvanrossum
- ref: e69c1f3e7a01d253e05b
- machine: linux-x86_64
- commit hash: e69c1f3
- commit date: 2023-01-26
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 250 ms: 1.34x faster                                                       |
| chameleon      | 9.17 ms                                                | 6.38 ms: 1.44x faster                                                      |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                     |
| html5lib       | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                      |
| tornado_http   | 128 ms                                                 | 94.1 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                  | 1.37x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 109 ms                                                 | 71.8 ms: 1.52x faster                                                      |
| nbody          | 144 ms                                                 | 95.4 ms: 1.51x faster                                                      |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.31x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                       |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                      |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                                       |
| regex_effbot   | 3.19 ms                                                | 3.54 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 286 us: 1.58x faster                                                       |
| unpickle_pure_python | 302 us                                                 | 196 us: 1.54x faster                                                       |
| json_dumps           | 13.4 ms                                                | 9.40 ms: 1.43x faster                                                      |
| xml_etree_process    | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                      |
| xml_etree_generate   | 93.8 ms                                                | 78.3 ms: 1.20x faster                                                      |
| json_loads           | 28.7 us                                                | 24.0 us: 1.20x faster                                                      |
| pickle_list          | 4.72 us                                                | 3.96 us: 1.19x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                       |
| unpickle             | 14.2 us                                                | 13.0 us: 1.09x faster                                                      |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.07x faster                                                       |
| pickle               | 10.2 us                                                | 10.0 us: 1.01x faster                                                      |
| unpickle_list        | 4.92 us                                                | 5.01 us: 1.02x slower                                                      |
| pickle_dict          | 27.6 us                                                | 30.4 us: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.90 ms: 1.58x faster                                                      |
| python_startup_no_site | 5.78 ms                                                | 6.44 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.70 ms: 1.51x faster                                                      |
| genshi_text     | 30.6 ms                                                | 21.2 ms: 1.45x faster                                                      |
| django_template | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                      |
| genshi_xml      | 63.7 ms                                                | 47.3 ms: 1.35x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.22 ms: 2.26x faster                                                      |
| logging_silent          | 176 ns                                                 | 92.5 ns: 1.91x faster                                                      |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                       |
| asyncio_tcp             | 914 ms                                                 | 501 ms: 1.83x faster                                                       |
| richards                | 75.2 ms                                                | 41.7 ms: 1.80x faster                                                      |
| pyflate                 | 676 ms                                                 | 399 ms: 1.70x faster                                                       |
| scimark_monte_carlo     | 109 ms                                                 | 65.2 ms: 1.66x faster                                                      |
| go                      | 226 ms                                                 | 136 ms: 1.65x faster                                                       |
| chaos                   | 106 ms                                                 | 64.0 ms: 1.65x faster                                                      |
| raytrace                | 467 ms                                                 | 284 ms: 1.64x faster                                                       |
| crypto_pyaes            | 117 ms                                                 | 72.1 ms: 1.62x faster                                                      |
| python_startup          | 14.1 ms                                                | 8.90 ms: 1.58x faster                                                      |
| pickle_pure_python      | 452 us                                                 | 286 us: 1.58x faster                                                       |
| hexiom                  | 9.43 ms                                                | 5.99 ms: 1.57x faster                                                      |
| unpickle_pure_python    | 302 us                                                 | 196 us: 1.54x faster                                                       |
| float                   | 109 ms                                                 | 71.8 ms: 1.52x faster                                                      |
| spectral_norm           | 150 ms                                                 | 98.9 ms: 1.51x faster                                                      |
| mako                    | 14.7 ms                                                | 9.70 ms: 1.51x faster                                                      |
| nbody                   | 144 ms                                                 | 95.4 ms: 1.51x faster                                                      |
| deepcopy_memo           | 51.7 us                                                | 34.3 us: 1.51x faster                                                      |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                                       |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.45x faster                                                     |
| genshi_text             | 30.6 ms                                                | 21.2 ms: 1.45x faster                                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                                      |
| html5lib                | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                      |
| chameleon               | 9.17 ms                                                | 6.38 ms: 1.44x faster                                                      |
| json_dumps              | 13.4 ms                                                | 9.40 ms: 1.43x faster                                                      |
| pprint_safe_repr        | 953 ms                                                 | 667 ms: 1.43x faster                                                       |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.42x faster                                                      |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                      |
| logging_simple          | 8.10 us                                                | 5.71 us: 1.42x faster                                                      |
| unpack_sequence         | 59.4 ns                                                | 41.9 ns: 1.42x faster                                                      |
| logging_format          | 8.85 us                                                | 6.31 us: 1.40x faster                                                      |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                       |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                                     |
| thrift                  | 1.03 ms                                                | 746 us: 1.39x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                      |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.95 ms: 1.38x faster                                                      |
| scimark_fft             | 421 ms                                                 | 308 ms: 1.37x faster                                                       |
| async_tree_memoization  | 855 ms                                                 | 626 ms: 1.37x faster                                                       |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                                     |
| tornado_http            | 128 ms                                                 | 94.1 ms: 1.36x faster                                                      |
| async_tree_none         | 711 ms                                                 | 523 ms: 1.36x faster                                                       |
| aiohttp                 | 1.34 ms                                                | 993 us: 1.35x faster                                                       |
| genshi_xml              | 63.7 ms                                                | 47.3 ms: 1.35x faster                                                      |
| gunicorn                | 1.43 ms                                                | 1.06 ms: 1.34x faster                                                      |
| 2to3                    | 335 ms                                                 | 250 ms: 1.34x faster                                                       |
| deepcopy                | 438 us                                                 | 327 us: 1.34x faster                                                       |
| fannkuch                | 488 ms                                                 | 367 ms: 1.33x faster                                                       |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                       |
| sqlglot_optimize        | 65.2 ms                                                | 50.7 ms: 1.29x faster                                                      |
| nqueens                 | 100 ms                                                 | 78.5 ms: 1.28x faster                                                      |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                     |
| deepcopy_reduce         | 3.79 us                                                | 3.00 us: 1.26x faster                                                      |
| async_tree_cpu_io_mixed | 949 ms                                                 | 756 ms: 1.26x faster                                                       |
| coroutines              | 31.6 ms                                                | 25.2 ms: 1.25x faster                                                      |
| dulwich_log             | 75.8 ms                                                | 62.1 ms: 1.22x faster                                                      |
| sympy_integrate         | 24.0 ms                                                | 19.7 ms: 1.22x faster                                                      |
| async_generators        | 426 ms                                                 | 351 ms: 1.22x faster                                                       |
| bench_thread_pool       | 946 us                                                 | 779 us: 1.21x faster                                                       |
| sympy_str               | 325 ms                                                 | 269 ms: 1.21x faster                                                       |
| xml_etree_generate      | 93.8 ms                                                | 78.3 ms: 1.20x faster                                                      |
| json_loads              | 28.7 us                                                | 24.0 us: 1.20x faster                                                      |
| pickle_list             | 4.72 us                                                | 3.96 us: 1.19x faster                                                      |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                       |
| sympy_expand            | 534 ms                                                 | 451 ms: 1.18x faster                                                       |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                      |
| json                    | 5.35 ms                                                | 4.63 ms: 1.15x faster                                                      |
| create_gc_cycles        | 1.65 ms                                                | 1.44 ms: 1.15x faster                                                      |
| djangocms               | 36.9 us                                                | 32.8 us: 1.12x faster                                                      |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                      |
| sqlite_synth            | 2.92 us                                                | 2.61 us: 1.12x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                       |
| unpickle                | 14.2 us                                                | 13.0 us: 1.09x faster                                                      |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                       |
| mdp                     | 2.74 sec                                               | 2.55 sec: 1.08x faster                                                     |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.07x faster                                                       |
| telco                   | 6.73 ms                                                | 6.30 ms: 1.07x faster                                                      |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                                       |
| generators              | 76.4 ms                                                | 75.1 ms: 1.02x faster                                                      |
| pickle                  | 10.2 us                                                | 10.0 us: 1.01x faster                                                      |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                       |
| unpickle_list           | 4.92 us                                                | 5.01 us: 1.02x slower                                                      |
| gc_traversal            | 3.53 ms                                                | 3.63 ms: 1.03x slower                                                      |
| pickle_dict             | 27.6 us                                                | 30.4 us: 1.10x slower                                                      |
| regex_effbot            | 3.19 ms                                                | 3.54 ms: 1.11x slower                                                      |
| python_startup_no_site  | 5.78 ms                                                | 6.44 ms: 1.11x slower                                                      |
| dask                    | 436 ms                                                 | 496 ms: 1.14x slower                                                       |
| coverage                | 74.7 ms                                                | 96.1 ms: 1.29x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                               |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230126-3.12.0a4+-e69c1f3/bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3.json: mypy
