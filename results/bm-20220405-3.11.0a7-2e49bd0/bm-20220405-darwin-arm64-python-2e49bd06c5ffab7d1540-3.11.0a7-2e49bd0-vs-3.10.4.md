
# Results vs. 3.10.4

- fork: python
- ref: 2e49bd06c5ffab7d1540
- machine: darwin-arm64
- commit hash: 2e49bd0
- commit date: 2022-04-05
- overall geometric mean: 1.21x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 162 ms: 1.25x faster                                                  |
| chameleon      | 5.84 ms                                                | 4.55 ms: 1.28x faster                                                 |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                |
| html5lib       | 44.1 ms                                                | 33.8 ms: 1.30x faster                                                 |
| tornado_http   | 91.9 ms                                                | 72.3 ms: 1.27x faster                                                 |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 66.1 ms: 1.43x faster                                                 |
| float          | 72.3 ms                                                | 52.8 ms: 1.37x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.5 ms: 1.28x faster                                                 |
| regex_effbot   | 2.45 ms                                                | 2.20 ms: 1.11x faster                                                 |
| regex_dna      | 160 ms                                                 | 171 ms: 1.07x slower                                                  |
| regex_v8       | 17.5 ms                                                | 19.8 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 199 us: 1.43x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 157 us: 1.29x faster                                                  |
| xml_etree_process    | 45.1 ms                                                | 35.2 ms: 1.28x faster                                                 |
| xml_etree_generate   | 54.3 ms                                                | 48.2 ms: 1.13x faster                                                 |
| json_dumps           | 8.38 ms                                                | 7.68 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 72.6 ms                                                | 67.3 ms: 1.08x faster                                                 |
| json_loads           | 16.9 us                                                | 15.9 us: 1.06x faster                                                 |
| xml_etree_parse      | 107 ms                                                 | 102 ms: 1.05x faster                                                  |
| pickle               | 7.36 us                                                | 7.15 us: 1.03x faster                                                 |
| pickle_dict          | 17.8 us                                                | 17.6 us: 1.01x faster                                                 |
| pickle_list          | 2.83 us                                                | 2.81 us: 1.01x faster                                                 |
| unpickle_list        | 2.66 us                                                | 2.65 us: 1.00x faster                                                 |
| unpickle             | 9.77 us                                                | 9.87 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.1 ms: 1.04x faster                                                 |
| python_startup_no_site | 9.73 ms                                                | 9.78 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 27.3 ms                                                | 21.2 ms: 1.29x faster                                                 |
| mako            | 10.5 ms                                                | 8.21 ms: 1.28x faster                                                 |
| genshi_xml      | 37.6 ms                                                | 30.5 ms: 1.23x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.1 ms: 1.22x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.25x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-darwin-arm64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.69 ms: 1.92x faster                                                 |
| logging_silent          | 119 ns                                                 | 69.6 ns: 1.71x faster                                                 |
| scimark_monte_carlo     | 72.2 ms                                                | 45.3 ms: 1.59x faster                                                 |
| richards                | 51.4 ms                                                | 32.6 ms: 1.57x faster                                                 |
| raytrace                | 328 ms                                                 | 212 ms: 1.54x faster                                                  |
| scimark_sor             | 127 ms                                                 | 82.2 ms: 1.54x faster                                                 |
| go                      | 165 ms                                                 | 108 ms: 1.53x faster                                                  |
| async_tree_memoization  | 493 ms                                                 | 323 ms: 1.53x faster                                                  |
| scimark_lu              | 110 ms                                                 | 72.2 ms: 1.52x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 703 ms: 1.45x faster                                                  |
| pyflate                 | 453 ms                                                 | 316 ms: 1.43x faster                                                  |
| pickle_pure_python      | 284 us                                                 | 199 us: 1.43x faster                                                  |
| nbody                   | 94.1 ms                                                | 66.1 ms: 1.43x faster                                                 |
| async_tree_none         | 402 ms                                                 | 283 ms: 1.42x faster                                                  |
| crypto_pyaes            | 78.0 ms                                                | 56.5 ms: 1.38x faster                                                 |
| logging_format          | 5.01 us                                                | 3.65 us: 1.37x faster                                                 |
| float                   | 72.3 ms                                                | 52.8 ms: 1.37x faster                                                 |
| thrift                  | 586 us                                                 | 432 us: 1.36x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.41 us: 1.36x faster                                                 |
| chaos                   | 66.8 ms                                                | 49.7 ms: 1.34x faster                                                 |
| deepcopy_memo           | 34.5 us                                                | 25.8 us: 1.34x faster                                                 |
| pprint_safe_repr        | 609 ms                                                 | 457 ms: 1.33x faster                                                  |
| pprint_pformat          | 1.24 sec                                               | 937 ms: 1.32x faster                                                  |
| spectral_norm           | 96.4 ms                                                | 73.4 ms: 1.31x faster                                                 |
| html5lib                | 44.1 ms                                                | 33.8 ms: 1.30x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.88 ms: 1.30x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 157 us: 1.29x faster                                                  |
| django_template         | 27.3 ms                                                | 21.2 ms: 1.29x faster                                                 |
| chameleon               | 5.84 ms                                                | 4.55 ms: 1.28x faster                                                 |
| xml_etree_process       | 45.1 ms                                                | 35.2 ms: 1.28x faster                                                 |
| regex_compile           | 96.6 ms                                                | 75.5 ms: 1.28x faster                                                 |
| mako                    | 10.5 ms                                                | 8.21 ms: 1.28x faster                                                 |
| pycparser               | 915 ms                                                 | 717 ms: 1.28x faster                                                  |
| tornado_http            | 91.9 ms                                                | 72.3 ms: 1.27x faster                                                 |
| 2to3                    | 202 ms                                                 | 162 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed | 670 ms                                                 | 541 ms: 1.24x faster                                                  |
| deepcopy_reduce         | 2.38 us                                                | 1.93 us: 1.23x faster                                                 |
| genshi_xml              | 37.6 ms                                                | 30.5 ms: 1.23x faster                                                 |
| mypy2                   | 308 ms                                                 | 251 ms: 1.23x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 30.3 ms: 1.22x faster                                                 |
| sqlalchemy_imperative   | 9.03 ms                                                | 7.37 ms: 1.22x faster                                                 |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                |
| deepcopy                | 278 us                                                 | 227 us: 1.22x faster                                                  |
| genshi_text             | 18.4 ms                                                | 15.1 ms: 1.22x faster                                                 |
| create_gc_cycles        | 876 us                                                 | 724 us: 1.21x faster                                                  |
| fannkuch                | 317 ms                                                 | 262 ms: 1.21x faster                                                  |
| unpack_sequence         | 38.7 ns                                                | 32.0 ns: 1.21x faster                                                 |
| async_generators        | 233 ms                                                 | 193 ms: 1.21x faster                                                  |
| sympy_integrate         | 13.4 ms                                                | 11.2 ms: 1.19x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.9 ms: 1.19x faster                                                 |
| aiohttp                 | 1.29 ms                                                | 1.09 ms: 1.19x faster                                                 |
| dask                    | 258 ms                                                 | 217 ms: 1.19x faster                                                  |
| sqlalchemy_declarative  | 74.8 ms                                                | 63.3 ms: 1.18x faster                                                 |
| coroutines              | 20.2 ms                                                | 17.3 ms: 1.17x faster                                                 |
| generators              | 32.9 ms                                                | 28.3 ms: 1.17x faster                                                 |
| gunicorn                | 1.34 ms                                                | 1.15 ms: 1.16x faster                                                 |
| scimark_fft             | 232 ms                                                 | 200 ms: 1.16x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.27 us: 1.16x faster                                                 |
| sqlglot_transpile       | 1.54 ms                                                | 1.33 ms: 1.15x faster                                                 |
| sympy_expand            | 276 ms                                                 | 241 ms: 1.15x faster                                                  |
| sympy_str               | 169 ms                                                 | 148 ms: 1.14x faster                                                  |
| sympy_sum               | 94.3 ms                                                | 82.6 ms: 1.14x faster                                                 |
| sqlglot_parse           | 1.33 ms                                                | 1.17 ms: 1.14x faster                                                 |
| sqlglot_normalize       | 197 ms                                                 | 173 ms: 1.14x faster                                                  |
| flaskblogging           | 2.75 ms                                                | 2.43 ms: 1.13x faster                                                 |
| xml_etree_generate      | 54.3 ms                                                | 48.2 ms: 1.13x faster                                                 |
| nqueens                 | 68.1 ms                                                | 60.6 ms: 1.12x faster                                                 |
| regex_effbot            | 2.45 ms                                                | 2.20 ms: 1.11x faster                                                 |
| pylint                  | 307 ms                                                 | 277 ms: 1.11x faster                                                  |
| bench_thread_pool       | 548 us                                                 | 499 us: 1.10x faster                                                  |
| json                    | 3.10 ms                                                | 2.82 ms: 1.10x faster                                                 |
| json_dumps              | 8.38 ms                                                | 7.68 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult | 3.47 ms                                                | 3.21 ms: 1.08x faster                                                 |
| xml_etree_iterparse     | 72.6 ms                                                | 67.3 ms: 1.08x faster                                                 |
| telco                   | 3.68 ms                                                | 3.41 ms: 1.08x faster                                                 |
| mdp                     | 1.67 sec                                               | 1.55 sec: 1.08x faster                                                |
| json_loads              | 16.9 us                                                | 15.9 us: 1.06x faster                                                 |
| xml_etree_parse         | 107 ms                                                 | 102 ms: 1.05x faster                                                  |
| meteor_contest          | 78.6 ms                                                | 74.7 ms: 1.05x faster                                                 |
| pathlib                 | 28.8 ms                                                | 27.5 ms: 1.05x faster                                                 |
| python_startup          | 12.6 ms                                                | 12.1 ms: 1.04x faster                                                 |
| asyncio_tcp             | 673 ms                                                 | 648 ms: 1.04x faster                                                  |
| pickle                  | 7.36 us                                                | 7.15 us: 1.03x faster                                                 |
| comprehensions          | 17.7 us                                                | 17.5 us: 1.01x faster                                                 |
| pickle_dict             | 17.8 us                                                | 17.6 us: 1.01x faster                                                 |
| pickle_list             | 2.83 us                                                | 2.81 us: 1.01x faster                                                 |
| unpickle_list           | 2.66 us                                                | 2.65 us: 1.00x faster                                                 |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| python_startup_no_site  | 9.73 ms                                                | 9.78 ms: 1.01x slower                                                 |
| gc_traversal            | 2.40 ms                                                | 2.41 ms: 1.01x slower                                                 |
| unpickle                | 9.77 us                                                | 9.87 us: 1.01x slower                                                 |
| bench_mp_pool           | 41.0 ms                                                | 43.2 ms: 1.05x slower                                                 |
| regex_dna               | 160 ms                                                 | 171 ms: 1.07x slower                                                  |
| regex_v8                | 17.5 ms                                                | 19.8 ms: 1.13x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.21x faster                                                          |
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x
