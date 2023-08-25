
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 4fe1c4b
- commit date: 2023-04-15
- overall geometric mean: 1.26x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 161 ms: 1.26x faster                                   |
| chameleon      | 5.84 ms                                                | 4.23 ms: 1.38x faster                                  |
| docutils       | 1.78 sec                                               | 1.45 sec: 1.23x faster                                 |
| html5lib       | 44.1 ms                                                | 34.9 ms: 1.26x faster                                  |
| tornado_http   | 91.9 ms                                                | 68.5 ms: 1.34x faster                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 56.7 ms: 1.66x faster                                  |
| float          | 72.3 ms                                                | 50.9 ms: 1.42x faster                                  |
| pidigits       | 282 ms                                                 | 280 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.33x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 72.3 ms: 1.34x faster                                  |
| regex_v8       | 17.5 ms                                                | 15.7 ms: 1.12x faster                                  |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.61 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 182 us: 1.56x faster                                   |
| unpickle_pure_python | 203 us                                                 | 137 us: 1.48x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.04 ms: 1.39x faster                                  |
| xml_etree_process    | 45.1 ms                                                | 34.5 ms: 1.31x faster                                  |
| xml_etree_generate   | 54.3 ms                                                | 49.0 ms: 1.11x faster                                  |
| xml_etree_parse      | 107 ms                                                 | 97.5 ms: 1.10x faster                                  |
| unpickle             | 9.77 us                                                | 8.99 us: 1.09x faster                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 68.4 ms: 1.06x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.03x faster                                  |
| unpickle_list        | 2.66 us                                                | 2.62 us: 1.02x faster                                  |
| pickle               | 7.36 us                                                | 7.50 us: 1.02x slower                                  |
| pickle_list          | 2.83 us                                                | 2.91 us: 1.03x slower                                  |
| pickle_dict          | 17.8 us                                                | 18.5 us: 1.04x slower                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 11.5 ms: 1.10x faster                                  |
| python_startup_no_site | 9.73 ms                                                | 9.51 ms: 1.02x faster                                  |
| Geometric mean         | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.04 ms: 1.49x faster                                  |
| genshi_xml      | 37.6 ms                                                | 26.4 ms: 1.43x faster                                  |
| genshi_text     | 18.4 ms                                                | 13.4 ms: 1.37x faster                                  |
| django_template | 27.3 ms                                                | 20.2 ms: 1.35x faster                                  |
| Geometric mean  | (ref)                                                  | 1.41x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-darwin-arm64-python-main-3.12.0a7+-4fe1c4b |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.50 ms: 2.06x faster                                  |
| logging_silent          | 119 ns                                                 | 62.1 ns: 1.92x faster                                  |
| richards                | 51.4 ms                                                | 30.7 ms: 1.68x faster                                  |
| nbody                   | 94.1 ms                                                | 56.7 ms: 1.66x faster                                  |
| scimark_lu              | 110 ms                                                 | 67.3 ms: 1.63x faster                                  |
| sqlglot_parse           | 1.33 ms                                                | 831 us: 1.60x faster                                   |
| asyncio_tcp             | 673 ms                                                 | 429 ms: 1.57x faster                                   |
| pickle_pure_python      | 284 us                                                 | 182 us: 1.56x faster                                   |
| raytrace                | 328 ms                                                 | 212 ms: 1.55x faster                                   |
| sqlglot_transpile       | 1.54 ms                                                | 992 us: 1.55x faster                                   |
| scimark_sor             | 127 ms                                                 | 81.8 ms: 1.55x faster                                  |
| hexiom                  | 6.32 ms                                                | 4.10 ms: 1.54x faster                                  |
| async_tree_memoization  | 493 ms                                                 | 320 ms: 1.54x faster                                   |
| go                      | 165 ms                                                 | 110 ms: 1.50x faster                                   |
| mako                    | 10.5 ms                                                | 7.04 ms: 1.49x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 137 us: 1.48x faster                                   |
| scimark_monte_carlo     | 72.2 ms                                                | 48.9 ms: 1.48x faster                                  |
| chaos                   | 66.8 ms                                                | 45.2 ms: 1.48x faster                                  |
| generators              | 32.9 ms                                                | 22.5 ms: 1.46x faster                                  |
| crypto_pyaes            | 78.0 ms                                                | 53.4 ms: 1.46x faster                                  |
| async_tree_none         | 402 ms                                                 | 277 ms: 1.45x faster                                   |
| genshi_xml              | 37.6 ms                                                | 26.4 ms: 1.43x faster                                  |
| async_tree_io           | 1.02 sec                                               | 716 ms: 1.42x faster                                   |
| spectral_norm           | 96.4 ms                                                | 67.8 ms: 1.42x faster                                  |
| float                   | 72.3 ms                                                | 50.9 ms: 1.42x faster                                  |
| deepcopy_memo           | 34.5 us                                                | 24.3 us: 1.42x faster                                  |
| pycparser               | 915 ms                                                 | 658 ms: 1.39x faster                                   |
| pyflate                 | 453 ms                                                 | 327 ms: 1.39x faster                                   |
| json_dumps              | 8.38 ms                                                | 6.04 ms: 1.39x faster                                  |
| pprint_safe_repr        | 609 ms                                                 | 440 ms: 1.38x faster                                   |
| chameleon               | 5.84 ms                                                | 4.23 ms: 1.38x faster                                  |
| pprint_pformat          | 1.24 sec                                               | 902 ms: 1.37x faster                                   |
| genshi_text             | 18.4 ms                                                | 13.4 ms: 1.37x faster                                  |
| django_template         | 27.3 ms                                                | 20.2 ms: 1.35x faster                                  |
| tornado_http            | 91.9 ms                                                | 68.5 ms: 1.34x faster                                  |
| regex_compile           | 96.6 ms                                                | 72.3 ms: 1.34x faster                                  |
| logging_simple          | 4.63 us                                                | 3.46 us: 1.34x faster                                  |
| thrift                  | 586 us                                                 | 440 us: 1.33x faster                                   |
| logging_format          | 5.01 us                                                | 3.79 us: 1.32x faster                                  |
| deepcopy                | 278 us                                                 | 211 us: 1.32x faster                                   |
| unpack_sequence         | 38.7 ns                                                | 29.5 ns: 1.31x faster                                  |
| xml_etree_process       | 45.1 ms                                                | 34.5 ms: 1.31x faster                                  |
| deepcopy_reduce         | 2.38 us                                                | 1.83 us: 1.30x faster                                  |
| scimark_fft             | 232 ms                                                 | 179 ms: 1.30x faster                                   |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.71 ms: 1.28x faster                                  |
| sqlalchemy_imperative   | 9.03 ms                                                | 7.07 ms: 1.28x faster                                  |
| sqlglot_optimize        | 38.0 ms                                                | 29.9 ms: 1.27x faster                                  |
| dulwich_log             | 37.1 ms                                                | 29.2 ms: 1.27x faster                                  |
| html5lib                | 44.1 ms                                                | 34.9 ms: 1.26x faster                                  |
| 2to3                    | 202 ms                                                 | 161 ms: 1.26x faster                                   |
| async_tree_cpu_io_mixed | 670 ms                                                 | 533 ms: 1.26x faster                                   |
| create_gc_cycles        | 876 us                                                 | 700 us: 1.25x faster                                   |
| fannkuch                | 317 ms                                                 | 257 ms: 1.23x faster                                   |
| docutils                | 1.78 sec                                               | 1.45 sec: 1.23x faster                                 |
| sqlalchemy_declarative  | 74.8 ms                                                | 61.6 ms: 1.22x faster                                  |
| mypy2                   | 308 ms                                                 | 256 ms: 1.21x faster                                   |
| bench_thread_pool       | 548 us                                                 | 455 us: 1.20x faster                                   |
| sqlglot_normalize       | 197 ms                                                 | 164 ms: 1.20x faster                                   |
| pylint                  | 307 ms                                                 | 256 ms: 1.20x faster                                   |
| sympy_integrate         | 13.4 ms                                                | 11.2 ms: 1.19x faster                                  |
| coroutines              | 20.2 ms                                                | 17.2 ms: 1.17x faster                                  |
| sympy_expand            | 276 ms                                                 | 237 ms: 1.16x faster                                   |
| sympy_str               | 169 ms                                                 | 148 ms: 1.14x faster                                   |
| nqueens                 | 68.1 ms                                                | 59.9 ms: 1.14x faster                                  |
| comprehensions          | 17.7 us                                                | 15.8 us: 1.12x faster                                  |
| regex_v8                | 17.5 ms                                                | 15.7 ms: 1.12x faster                                  |
| json                    | 3.10 ms                                                | 2.78 ms: 1.11x faster                                  |
| sympy_sum               | 94.3 ms                                                | 84.9 ms: 1.11x faster                                  |
| mdp                     | 1.67 sec                                               | 1.50 sec: 1.11x faster                                 |
| xml_etree_generate      | 54.3 ms                                                | 49.0 ms: 1.11x faster                                  |
| meteor_contest          | 78.6 ms                                                | 71.3 ms: 1.10x faster                                  |
| xml_etree_parse         | 107 ms                                                 | 97.5 ms: 1.10x faster                                  |
| python_startup          | 12.6 ms                                                | 11.5 ms: 1.10x faster                                  |
| telco                   | 3.68 ms                                                | 3.36 ms: 1.10x faster                                  |
| sqlite_synth            | 1.47 us                                                | 1.35 us: 1.09x faster                                  |
| unpickle                | 9.77 us                                                | 8.99 us: 1.09x faster                                  |
| regex_dna               | 160 ms                                                 | 149 ms: 1.07x faster                                   |
| xml_etree_iterparse     | 72.6 ms                                                | 68.4 ms: 1.06x faster                                  |
| pathlib                 | 28.8 ms                                                | 27.2 ms: 1.06x faster                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.03x faster                                  |
| python_startup_no_site  | 9.73 ms                                                | 9.51 ms: 1.02x faster                                  |
| unpickle_list           | 2.66 us                                                | 2.62 us: 1.02x faster                                  |
| pidigits                | 282 ms                                                 | 280 ms: 1.01x faster                                   |
| gc_traversal            | 2.40 ms                                                | 2.43 ms: 1.01x slower                                  |
| pickle                  | 7.36 us                                                | 7.50 us: 1.02x slower                                  |
| pickle_list             | 2.83 us                                                | 2.91 us: 1.03x slower                                  |
| pickle_dict             | 17.8 us                                                | 18.5 us: 1.04x slower                                  |
| regex_effbot            | 2.45 ms                                                | 2.61 ms: 1.07x slower                                  |
| bench_mp_pool           | 41.0 ms                                                | 45.1 ms: 1.10x slower                                  |
| async_generators        | 233 ms                                                 | 257 ms: 1.10x slower                                   |
| dask                    | 258 ms                                                 | 314 ms: 1.22x slower                                   |
| coverage                | 40.8 ms                                                | 52.1 ms: 1.28x slower                                  |
| Geometric mean          | (ref)                                                  | 1.26x faster                                           |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x
