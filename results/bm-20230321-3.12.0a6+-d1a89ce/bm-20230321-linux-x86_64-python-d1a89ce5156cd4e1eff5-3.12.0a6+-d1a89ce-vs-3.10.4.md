
# Results vs. 3.10.4

- fork: python
- ref: d1a89ce5156cd4e1eff5
- machine: linux-x86_64
- commit hash: d1a89ce
- commit date: 2023-03-21
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.35 ms: 1.43x faster                                                  |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                 |
| html5lib       | 85.9 ms                                                | 60.5 ms: 1.42x faster                                                  |
| tornado_http   | 127 ms                                                 | 91.0 ms: 1.40x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.7 ms: 1.61x faster                                                  |
| float          | 111 ms                                                 | 74.3 ms: 1.49x faster                                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                  |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.42 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 284 us: 1.60x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.51x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.59 ms: 1.41x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 56.0 ms: 1.34x faster                                                  |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 80.8 ms: 1.17x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 151 ms: 1.08x faster                                                   |
| pickle_list          | 4.56 us                                                | 4.23 us: 1.08x faster                                                  |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                                  |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                                  |
| unpickle_list        | 4.82 us                                                | 5.05 us: 1.05x slower                                                  |
| pickle_dict          | 27.3 us                                                | 31.2 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.88 ms: 1.59x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.56 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.1 ms: 1.46x faster                                                  |
| genshi_text     | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                  |
| django_template | 45.9 ms                                                | 33.2 ms: 1.38x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 48.0 ms: 1.32x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.7 ms: 2.58x faster                                                  |
| deltablue               | 7.42 ms                                                | 3.17 ms: 2.34x faster                                                  |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                   |
| logging_silent          | 175 ns                                                 | 94.8 ns: 1.85x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 504 ms: 1.84x faster                                                   |
| richards                | 74.9 ms                                                | 43.2 ms: 1.73x faster                                                  |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                                   |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                                   |
| scimark_monte_carlo     | 108 ms                                                 | 66.2 ms: 1.64x faster                                                  |
| spectral_norm           | 150 ms                                                 | 92.0 ms: 1.63x faster                                                  |
| pyflate                 | 673 ms                                                 | 416 ms: 1.62x faster                                                   |
| chaos                   | 106 ms                                                 | 65.8 ms: 1.62x faster                                                  |
| nbody                   | 142 ms                                                 | 87.7 ms: 1.61x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 284 us: 1.60x faster                                                   |
| python_startup          | 14.2 ms                                                | 8.88 ms: 1.59x faster                                                  |
| crypto_pyaes            | 118 ms                                                 | 74.9 ms: 1.58x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.17 ms: 1.54x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 34.5 us: 1.52x faster                                                  |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.52x faster                                                   |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.51x faster                                                   |
| float                   | 111 ms                                                 | 74.3 ms: 1.49x faster                                                  |
| mako                    | 14.8 ms                                                | 10.1 ms: 1.46x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 44.4 ns: 1.46x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.43 ms: 1.44x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.62 us: 1.44x faster                                                  |
| coroutines              | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                  |
| chameleon               | 9.06 ms                                                | 6.35 ms: 1.43x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.42x faster                                                  |
| logging_format          | 8.91 us                                                | 6.26 us: 1.42x faster                                                  |
| html5lib                | 85.9 ms                                                | 60.5 ms: 1.42x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                                 |
| json_dumps              | 13.5 ms                                                | 9.59 ms: 1.41x faster                                                  |
| genshi_text             | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                  |
| tornado_http            | 127 ms                                                 | 91.0 ms: 1.40x faster                                                  |
| scimark_fft             | 424 ms                                                 | 303 ms: 1.40x faster                                                   |
| pprint_safe_repr        | 955 ms                                                 | 691 ms: 1.38x faster                                                   |
| django_template         | 45.9 ms                                                | 33.2 ms: 1.38x faster                                                  |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                  |
| async_tree_memoization  | 854 ms                                                 | 624 ms: 1.37x faster                                                   |
| async_tree_none         | 717 ms                                                 | 523 ms: 1.37x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                                 |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.36x faster                                                 |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                  |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                   |
| thrift                  | 1.03 ms                                                | 771 us: 1.34x faster                                                   |
| deepcopy                | 442 us                                                 | 330 us: 1.34x faster                                                   |
| xml_etree_process       | 74.9 ms                                                | 56.0 ms: 1.34x faster                                                  |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                   |
| fannkuch                | 486 ms                                                 | 368 ms: 1.32x faster                                                   |
| genshi_xml              | 63.3 ms                                                | 48.0 ms: 1.32x faster                                                  |
| deepcopy_reduce         | 3.82 us                                                | 2.95 us: 1.30x faster                                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 735 ms: 1.29x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                   |
| mypy2                   | 428 ms                                                 | 333 ms: 1.29x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.9 ms: 1.28x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.28 ms: 1.27x faster                                                  |
| nqueens                 | 100 ms                                                 | 79.7 ms: 1.26x faster                                                  |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                 |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                   |
| dulwich_log             | 75.9 ms                                                | 63.0 ms: 1.21x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 788 us: 1.20x faster                                                   |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.7 ms: 1.20x faster                                                  |
| sympy_expand            | 545 ms                                                 | 456 ms: 1.19x faster                                                   |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                                  |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.19x faster                                                  |
| json                    | 5.42 ms                                                | 4.57 ms: 1.19x faster                                                  |
| sympy_str               | 328 ms                                                 | 282 ms: 1.17x faster                                                   |
| xml_etree_generate      | 94.2 ms                                                | 80.8 ms: 1.17x faster                                                  |
| comprehensions          | 26.8 us                                                | 23.4 us: 1.15x faster                                                  |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                  |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                  |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.12x faster                                                   |
| sympy_sum               | 185 ms                                                 | 165 ms: 1.12x faster                                                   |
| djangocms               | 35.9 us                                                | 32.5 us: 1.11x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| regex_dna               | 222 ms                                                 | 204 ms: 1.09x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 151 ms: 1.08x faster                                                   |
| pickle_list             | 4.56 us                                                | 4.23 us: 1.08x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.63 sec: 1.07x faster                                                 |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                                  |
| async_generators        | 425 ms                                                 | 417 ms: 1.02x faster                                                   |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| gc_traversal            | 3.84 ms                                                | 3.84 ms: 1.00x faster                                                  |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                  |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                                  |
| unpickle_list           | 4.82 us                                                | 5.05 us: 1.05x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.42 ms: 1.06x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.56 ms: 1.13x slower                                                  |
| pickle_dict             | 27.3 us                                                | 31.2 us: 1.14x slower                                                  |
| dask                    | 423 ms                                                 | 501 ms: 1.19x slower                                                   |
| coverage                | 72.8 ms                                                | 93.4 ms: 1.28x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (1): telco
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x
