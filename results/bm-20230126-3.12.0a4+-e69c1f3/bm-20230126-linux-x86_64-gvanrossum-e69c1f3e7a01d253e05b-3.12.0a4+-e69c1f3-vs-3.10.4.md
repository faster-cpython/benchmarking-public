
# Results vs. 3.10.4

- fork: gvanrossum
- ref: e69c1f3e7a01d253e05b
- machine: linux-x86_64
- commit hash: e69c1f3
- commit date: 2023-01-26
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 250 ms: 1.34x faster                                                       |
| chameleon      | 9.06 ms                                                | 6.38 ms: 1.42x faster                                                      |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                     |
| html5lib       | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                      |
| tornado_http   | 127 ms                                                 | 94.1 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                  | 1.36x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 71.8 ms: 1.54x faster                                                      |
| nbody          | 142 ms                                                 | 95.4 ms: 1.48x faster                                                      |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.31x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                       |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                      |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                                       |
| regex_effbot   | 3.23 ms                                                | 3.54 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.59x faster                                                       |
| unpickle_pure_python | 300 us                                                 | 196 us: 1.54x faster                                                       |
| json_dumps           | 13.5 ms                                                | 9.40 ms: 1.44x faster                                                      |
| xml_etree_process    | 74.9 ms                                                | 54.0 ms: 1.39x faster                                                      |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                                      |
| xml_etree_generate   | 94.2 ms                                                | 78.3 ms: 1.20x faster                                                      |
| pickle_list          | 4.56 us                                                | 3.96 us: 1.15x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                       |
| unpickle             | 14.1 us                                                | 13.0 us: 1.09x faster                                                      |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                       |
| pickle               | 10.3 us                                                | 10.0 us: 1.03x faster                                                      |
| unpickle_list        | 4.82 us                                                | 5.01 us: 1.04x slower                                                      |
| pickle_dict          | 27.3 us                                                | 30.4 us: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.90 ms: 1.59x faster                                                      |
| python_startup_no_site | 5.82 ms                                                | 6.44 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.70 ms: 1.52x faster                                                      |
| genshi_text     | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                      |
| django_template | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                      |
| genshi_xml      | 63.3 ms                                                | 47.3 ms: 1.34x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.22 ms: 2.30x faster                                                      |
| logging_silent          | 175 ns                                                 | 92.5 ns: 1.89x faster                                                      |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                       |
| asyncio_tcp             | 925 ms                                                 | 501 ms: 1.85x faster                                                       |
| richards                | 74.9 ms                                                | 41.7 ms: 1.80x faster                                                      |
| pyflate                 | 673 ms                                                 | 399 ms: 1.69x faster                                                       |
| go                      | 229 ms                                                 | 136 ms: 1.68x faster                                                       |
| scimark_monte_carlo     | 108 ms                                                 | 65.2 ms: 1.66x faster                                                      |
| chaos                   | 106 ms                                                 | 64.0 ms: 1.66x faster                                                      |
| crypto_pyaes            | 118 ms                                                 | 72.1 ms: 1.64x faster                                                      |
| raytrace                | 464 ms                                                 | 284 ms: 1.63x faster                                                       |
| hexiom                  | 9.53 ms                                                | 5.99 ms: 1.59x faster                                                      |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.59x faster                                                       |
| python_startup          | 14.2 ms                                                | 8.90 ms: 1.59x faster                                                      |
| unpack_sequence         | 64.7 ns                                                | 41.9 ns: 1.54x faster                                                      |
| float                   | 111 ms                                                 | 71.8 ms: 1.54x faster                                                      |
| unpickle_pure_python    | 300 us                                                 | 196 us: 1.54x faster                                                       |
| deepcopy_memo           | 52.3 us                                                | 34.3 us: 1.53x faster                                                      |
| mako                    | 14.8 ms                                                | 9.70 ms: 1.52x faster                                                      |
| spectral_norm           | 150 ms                                                 | 98.9 ms: 1.52x faster                                                      |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                       |
| nbody                   | 142 ms                                                 | 95.4 ms: 1.48x faster                                                      |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                                     |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.45x faster                                                      |
| json_dumps              | 13.5 ms                                                | 9.40 ms: 1.44x faster                                                      |
| html5lib                | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                      |
| sqlglot_transpile       | 2.45 ms                                                | 1.70 ms: 1.44x faster                                                      |
| genshi_text             | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                      |
| pprint_safe_repr        | 955 ms                                                 | 667 ms: 1.43x faster                                                       |
| chameleon               | 9.06 ms                                                | 6.38 ms: 1.42x faster                                                      |
| logging_simple          | 8.07 us                                                | 5.71 us: 1.41x faster                                                      |
| logging_format          | 8.91 us                                                | 6.31 us: 1.41x faster                                                      |
| django_template         | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                      |
| aiohttp                 | 1.38 ms                                                | 993 us: 1.39x faster                                                       |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                       |
| xml_etree_process       | 74.9 ms                                                | 54.0 ms: 1.39x faster                                                      |
| thrift                  | 1.03 ms                                                | 746 us: 1.39x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.95 ms: 1.38x faster                                                      |
| scimark_fft             | 424 ms                                                 | 308 ms: 1.38x faster                                                       |
| gunicorn                | 1.46 ms                                                | 1.06 ms: 1.37x faster                                                      |
| async_tree_none         | 717 ms                                                 | 523 ms: 1.37x faster                                                       |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.37x faster                                                     |
| async_tree_memoization  | 854 ms                                                 | 626 ms: 1.37x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.36x faster                                                     |
| tornado_http            | 127 ms                                                 | 94.1 ms: 1.35x faster                                                      |
| deepcopy                | 442 us                                                 | 327 us: 1.35x faster                                                       |
| 2to3                    | 336 ms                                                 | 250 ms: 1.34x faster                                                       |
| genshi_xml              | 63.3 ms                                                | 47.3 ms: 1.34x faster                                                      |
| fannkuch                | 486 ms                                                 | 367 ms: 1.33x faster                                                       |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 50.7 ms: 1.29x faster                                                      |
| nqueens                 | 100 ms                                                 | 78.5 ms: 1.27x faster                                                      |
| deepcopy_reduce         | 3.82 us                                                | 3.00 us: 1.27x faster                                                      |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                     |
| coroutines              | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                      |
| async_tree_cpu_io_mixed | 951 ms                                                 | 756 ms: 1.26x faster                                                       |
| sympy_integrate         | 24.3 ms                                                | 19.7 ms: 1.23x faster                                                      |
| dulwich_log             | 75.9 ms                                                | 62.1 ms: 1.22x faster                                                      |
| sympy_str               | 328 ms                                                 | 269 ms: 1.22x faster                                                       |
| bench_thread_pool       | 947 us                                                 | 779 us: 1.22x faster                                                       |
| async_generators        | 425 ms                                                 | 351 ms: 1.21x faster                                                       |
| sympy_expand            | 545 ms                                                 | 451 ms: 1.21x faster                                                       |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                                      |
| xml_etree_generate      | 94.2 ms                                                | 78.3 ms: 1.20x faster                                                      |
| sympy_sum               | 185 ms                                                 | 155 ms: 1.19x faster                                                       |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                      |
| json                    | 5.42 ms                                                | 4.63 ms: 1.17x faster                                                      |
| create_gc_cycles        | 1.67 ms                                                | 1.44 ms: 1.16x faster                                                      |
| pickle_list             | 4.56 us                                                | 3.96 us: 1.15x faster                                                      |
| sqlite_synth            | 2.93 us                                                | 2.61 us: 1.13x faster                                                      |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.55 sec: 1.11x faster                                                     |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                                       |
| djangocms               | 35.9 us                                                | 32.8 us: 1.10x faster                                                      |
| unpickle                | 14.1 us                                                | 13.0 us: 1.09x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                       |
| regex_dna               | 222 ms                                                 | 208 ms: 1.07x faster                                                       |
| gc_traversal            | 3.84 ms                                                | 3.63 ms: 1.06x faster                                                      |
| telco                   | 6.54 ms                                                | 6.30 ms: 1.04x faster                                                      |
| pickle                  | 10.3 us                                                | 10.0 us: 1.03x faster                                                      |
| generators              | 76.8 ms                                                | 75.1 ms: 1.02x faster                                                      |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                      |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                       |
| unpickle_list           | 4.82 us                                                | 5.01 us: 1.04x slower                                                      |
| regex_effbot            | 3.23 ms                                                | 3.54 ms: 1.10x slower                                                      |
| python_startup_no_site  | 5.82 ms                                                | 6.44 ms: 1.11x slower                                                      |
| pickle_dict             | 27.3 us                                                | 30.4 us: 1.12x slower                                                      |
| dask                    | 423 ms                                                 | 496 ms: 1.17x slower                                                       |
| coverage                | 72.8 ms                                                | 96.1 ms: 1.32x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                               |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230126-3.12.0a4+-e69c1f3/bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
