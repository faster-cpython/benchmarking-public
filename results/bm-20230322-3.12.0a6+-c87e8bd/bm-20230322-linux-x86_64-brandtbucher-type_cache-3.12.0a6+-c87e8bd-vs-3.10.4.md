
# Results vs. 3.10.4

- fork: brandtbucher
- ref: type_cache
- machine: linux-x86_64
- commit hash: c87e8bd
- commit date: 2023-03-22
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 253 ms: 1.32x faster                                               |
| chameleon      | 9.17 ms                                                | 6.64 ms: 1.38x faster                                              |
| docutils       | 3.18 sec                                               | 2.56 sec: 1.24x faster                                             |
| html5lib       | 85.9 ms                                                | 61.9 ms: 1.39x faster                                              |
| tornado_http   | 128 ms                                                 | 91.7 ms: 1.40x faster                                              |
| Geometric mean | (ref)                                                  | 1.34x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 90.6 ms: 1.59x faster                                              |
| float          | 109 ms                                                 | 74.4 ms: 1.46x faster                                              |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.33x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                               |
| regex_v8       | 25.0 ms                                                | 22.8 ms: 1.10x faster                                              |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                               |
| regex_effbot   | 3.19 ms                                                | 3.57 ms: 1.12x slower                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 290 us: 1.56x faster                                               |
| unpickle_pure_python | 302 us                                                 | 203 us: 1.48x faster                                               |
| json_dumps           | 13.4 ms                                                | 9.70 ms: 1.39x faster                                              |
| xml_etree_process    | 74.5 ms                                                | 57.3 ms: 1.30x faster                                              |
| json_loads           | 28.7 us                                                | 24.2 us: 1.18x faster                                              |
| xml_etree_generate   | 93.8 ms                                                | 81.7 ms: 1.15x faster                                              |
| pickle_list          | 4.72 us                                                | 4.21 us: 1.12x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.08x faster                                               |
| unpickle             | 14.2 us                                                | 13.4 us: 1.06x faster                                              |
| pickle               | 10.2 us                                                | 10.2 us: 1.01x slower                                              |
| unpickle_list        | 4.92 us                                                | 5.20 us: 1.06x slower                                              |
| pickle_dict          | 27.6 us                                                | 31.1 us: 1.13x slower                                              |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.88 ms: 1.59x faster                                              |
| python_startup_no_site | 5.78 ms                                                | 6.56 ms: 1.14x slower                                              |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.0 ms: 1.46x faster                                              |
| genshi_text     | 30.6 ms                                                | 21.8 ms: 1.40x faster                                              |
| django_template | 46.3 ms                                                | 33.2 ms: 1.40x faster                                              |
| genshi_xml      | 63.7 ms                                                | 48.1 ms: 1.32x faster                                              |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.4 ms: 2.60x faster                                              |
| deltablue               | 7.28 ms                                                | 3.33 ms: 2.18x faster                                              |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                               |
| logging_silent          | 176 ns                                                 | 97.0 ns: 1.82x faster                                              |
| asyncio_tcp             | 914 ms                                                 | 509 ms: 1.80x faster                                               |
| richards                | 75.2 ms                                                | 44.0 ms: 1.71x faster                                              |
| go                      | 226 ms                                                 | 135 ms: 1.68x faster                                               |
| spectral_norm           | 150 ms                                                 | 90.4 ms: 1.65x faster                                              |
| pyflate                 | 676 ms                                                 | 417 ms: 1.62x faster                                               |
| scimark_monte_carlo     | 109 ms                                                 | 67.8 ms: 1.60x faster                                              |
| raytrace                | 467 ms                                                 | 293 ms: 1.59x faster                                               |
| nbody                   | 144 ms                                                 | 90.6 ms: 1.59x faster                                              |
| python_startup          | 14.1 ms                                                | 8.88 ms: 1.59x faster                                              |
| chaos                   | 106 ms                                                 | 67.0 ms: 1.58x faster                                              |
| hexiom                  | 9.43 ms                                                | 6.04 ms: 1.56x faster                                              |
| pickle_pure_python      | 452 us                                                 | 290 us: 1.56x faster                                               |
| crypto_pyaes            | 117 ms                                                 | 75.3 ms: 1.55x faster                                              |
| unpickle_pure_python    | 302 us                                                 | 203 us: 1.48x faster                                               |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.48x faster                                               |
| deepcopy_memo           | 51.7 us                                                | 34.9 us: 1.48x faster                                              |
| mako                    | 14.7 ms                                                | 10.0 ms: 1.46x faster                                              |
| float                   | 109 ms                                                 | 74.4 ms: 1.46x faster                                              |
| coroutines              | 31.6 ms                                                | 22.5 ms: 1.40x faster                                              |
| genshi_text             | 30.6 ms                                                | 21.8 ms: 1.40x faster                                              |
| sqlglot_parse           | 2.04 ms                                                | 1.46 ms: 1.40x faster                                              |
| tornado_http            | 128 ms                                                 | 91.7 ms: 1.40x faster                                              |
| django_template         | 46.3 ms                                                | 33.2 ms: 1.40x faster                                              |
| pprint_pformat          | 1.98 sec                                               | 1.42 sec: 1.39x faster                                             |
| html5lib                | 85.9 ms                                                | 61.9 ms: 1.39x faster                                              |
| sqlglot_transpile       | 2.43 ms                                                | 1.75 ms: 1.39x faster                                              |
| json_dumps              | 13.4 ms                                                | 9.70 ms: 1.39x faster                                              |
| chameleon               | 9.17 ms                                                | 6.64 ms: 1.38x faster                                              |
| pprint_safe_repr        | 953 ms                                                 | 693 ms: 1.38x faster                                               |
| logging_simple          | 8.10 us                                                | 5.90 us: 1.37x faster                                              |
| scimark_fft             | 421 ms                                                 | 307 ms: 1.37x faster                                               |
| logging_format          | 8.85 us                                                | 6.47 us: 1.37x faster                                              |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                             |
| unpack_sequence         | 59.4 ns                                                | 44.0 ns: 1.35x faster                                              |
| async_tree_none         | 711 ms                                                 | 529 ms: 1.35x faster                                               |
| 2to3                    | 335 ms                                                 | 253 ms: 1.32x faster                                               |
| genshi_xml              | 63.7 ms                                                | 48.1 ms: 1.32x faster                                              |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                               |
| pycparser               | 1.53 sec                                               | 1.16 sec: 1.32x faster                                             |
| deepcopy                | 438 us                                                 | 333 us: 1.31x faster                                               |
| fannkuch                | 488 ms                                                 | 374 ms: 1.30x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 57.3 ms: 1.30x faster                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.22 ms: 1.29x faster                                              |
| deepcopy_reduce         | 3.79 us                                                | 2.94 us: 1.29x faster                                              |
| async_tree_memoization  | 855 ms                                                 | 667 ms: 1.28x faster                                               |
| mypy2                   | 430 ms                                                 | 336 ms: 1.28x faster                                               |
| async_tree_cpu_io_mixed | 949 ms                                                 | 746 ms: 1.27x faster                                               |
| thrift                  | 1.03 ms                                                | 816 us: 1.27x faster                                               |
| sqlglot_optimize        | 65.2 ms                                                | 52.2 ms: 1.25x faster                                              |
| sqlglot_normalize       | 134 ms                                                 | 108 ms: 1.25x faster                                               |
| nqueens                 | 100 ms                                                 | 80.5 ms: 1.24x faster                                              |
| docutils                | 3.18 sec                                               | 2.56 sec: 1.24x faster                                             |
| dulwich_log             | 75.8 ms                                                | 63.4 ms: 1.20x faster                                              |
| bench_thread_pool       | 946 us                                                 | 794 us: 1.19x faster                                               |
| json_loads              | 28.7 us                                                | 24.2 us: 1.18x faster                                              |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.17x faster                                              |
| xml_etree_generate      | 93.8 ms                                                | 81.7 ms: 1.15x faster                                              |
| sympy_expand            | 534 ms                                                 | 465 ms: 1.15x faster                                               |
| sympy_str               | 325 ms                                                 | 284 ms: 1.14x faster                                               |
| json                    | 5.35 ms                                                | 4.70 ms: 1.14x faster                                              |
| pickle_list             | 4.72 us                                                | 4.21 us: 1.12x faster                                              |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                              |
| sqlite_synth            | 2.92 us                                                | 2.62 us: 1.12x faster                                              |
| create_gc_cycles        | 1.65 ms                                                | 1.49 ms: 1.11x faster                                              |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.10x faster                                               |
| regex_v8                | 25.0 ms                                                | 22.8 ms: 1.10x faster                                              |
| mdp                     | 2.74 sec                                               | 2.51 sec: 1.09x faster                                             |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                               |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.08x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 152 ms: 1.08x faster                                               |
| unpickle                | 14.2 us                                                | 13.4 us: 1.06x faster                                              |
| telco                   | 6.73 ms                                                | 6.53 ms: 1.03x faster                                              |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                               |
| async_generators        | 426 ms                                                 | 417 ms: 1.02x faster                                               |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                               |
| pickle                  | 10.2 us                                                | 10.2 us: 1.01x slower                                              |
| unpickle_list           | 4.92 us                                                | 5.20 us: 1.06x slower                                              |
| regex_effbot            | 3.19 ms                                                | 3.57 ms: 1.12x slower                                              |
| pickle_dict             | 27.6 us                                                | 31.1 us: 1.13x slower                                              |
| gc_traversal            | 3.53 ms                                                | 3.98 ms: 1.13x slower                                              |
| python_startup_no_site  | 5.78 ms                                                | 6.56 ms: 1.14x slower                                              |
| dask                    | 436 ms                                                 | 509 ms: 1.17x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                       |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, coverage, djangocms, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230322-3.12.0a6+-c87e8bd/bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd.json: comprehensions
